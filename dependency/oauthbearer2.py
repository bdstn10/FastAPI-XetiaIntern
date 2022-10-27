import logging
from os import path
from typing import Any, Dict
from fastapi import Request, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from tortoise.exceptions import IntegrityError
from tortoise.query_utils import Q

from app.configs import config
from helper.rpc_client import RPCClient
from database.schema.main_model import Entity, User, UserEntityRole
from model.login import Login

logger = logging.getLogger()


# Reading public RS256 key
def read_pubkey() -> str:
    # check if verifier is None
    if not config.verifier:
        return ""

    # Try open and reading verifier key
    pubkey_path = path.join(config.root_dir, 'secrets', config.verifier)
    try:
        with open(pubkey_path, mode="r") as pubkey:
            key = pubkey.read()
            return key
    # Exception occurs when file not found
    except FileNotFoundError:
        logger.error(f"Verifier key not found ({pubkey_path})")
        return ""


class TokenBearer(HTTPBearer):
    """
    Oauth2 Bearer token dependency
    """

    def __init__(
        self,
        auto_error: bool = True,
        include_raw: bool = False,

    ) -> None:
        super().__init__(auto_error=auto_error)
        self.user = None
        self.include_raw = include_raw

    async def __call__(self, request: Request) -> Any:
        credential: HTTPAuthorizationCredentials = await super().__call__(request)

        # if credentials return empty string or None
        if not credential and not self.auto_error:
            return None

        return await self.decode_credential(credential.credentials)

    async def decode_credential(self, credentials: str):
        """
        Decode credential (Token)
        """
        try:
            payload = jwt.decode(
                credentials,
                read_pubkey(),
                algorithms=config.algorithm,
            )
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Bearer token expired",
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid bearer token",
            )

        # Check if entity is exists in database
        await self.check_entity(payload)

        # Ensure user is exists in database
        await self.check_user(payload)

        # assign permission if it first time
        user = await User.get(Q(pk=payload["user_id"]))
        self.user = user
        user_entities = payload["user_entities"]

        for entity in user_entities:
            await UserEntityRole.get_or_create(
                {"role": entity["role"]},
                user=user,
                entity_id=entity["entity"],
            )

        return Login(
            user = user,
            raw_token = credentials if self.include_raw else None 
        )

    async def check_entity(self, payload: Dict) -> None:
        """
        Ensure Entity is exists
        """
        try:
            user_entity = payload["user_entities"]
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token Payload",
            )

        for entity in user_entity:
            exists = await Entity.exists(Q(pk=entity["entity"]))

            # if entity is not exists then request to user service trough RPC
            if not exists:
                rpc_client = RPCClient(
                    command="fetch_entities",
                    route_key="user_rpc_queue",
                )
                response = rpc_client.get_response({"entity_ids": [entity["entity"]]})

                if response["meta"]["code"] != 200:
                    logger.error(
                        f"Failed fetch entity, {response['meta']['message']}",
                        detail="Failed fetching entity",
                    )
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="Failed Fetching Entity"
                    )

                if len(response["response"]) < 1:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Entity not found"
                    )
                
                _entity = response["response"][0]
                entity_obj = Entity(
                    id=_entity["id"],
                    name=_entity["name"],
                    slug=_entity["slug"],
                    type=_entity["entity_type"],
                    country=_entity["country"],
                    currency=_entity["currency"],
                )

                try:
                    await entity_obj.save()
                except IntegrityError:
                    pass

    async def check_user(self, payload: Dict) -> None:
        """
        Ensure User exists
        """
        user_id = payload["user_id"]

        # check user existance
        exists = await User.exists(Q(pk=user_id))

        if not exists:
            rpc_client = RPCClient(command="fetch_users", route_key="user_rpc_queue")
            response = rpc_client.get_response({"user_ids": [user_id]})

            if response["meta"]["code"] != 200:
                logger.error(f"Failed to fetch user, {response['meta']['message']}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Failed fetching user info",
                )

            if len(response["response"]) < 1:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            
            _user = response["response"][0]
            user_obj = User(
                id=_user["id"],
                first_name=_user["first_name"],
                last_name=_user["last_name"],
                slug=_user["slug"],
                email=_user["email"],
                country=_user["country"],
                currency=_user["currency"]
            )

            try:
                await user_obj.save()
            except IntegrityError:
                pass
