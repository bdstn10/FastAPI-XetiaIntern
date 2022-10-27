from typing import List
from fastapi import Header, HTTPException, status
from tortoise.exceptions import DoesNotExist
from database.schema.main_model import Entity, User, UserEntityRole

async def entity_header(entity: str = Header (None, description="entity slug")):
    if entity:
        try:
            e = await Entity.get(slug=entity)
        except DoesNotExist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entity not found"
            )
    return None if entity == None else e

async def entity_header_req(
    entity: str = Header (..., description="entity slug"),
):
    try:
        e = await Entity.get(slug=entity)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found"
        )
    return e

async def validate_role(user: User, entity: Entity, role: List[int]):
    user_role = await UserEntityRole.get(user_id=user.id, entity_id=entity.id)
    
    if user_role.role not in role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Require entity role level {' and '.join(map(role_name, role))}"
        )
    return user_role.role

def role_name(role_code):
    if role_code == 1:
        return "admin"
    elif role_code == 2:
        return "staff"
    else:
        return "member"
