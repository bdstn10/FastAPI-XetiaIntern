from uuid import UUID
from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    slug: str
    email: str
    country: str
    currency: str


class Login(BaseModel):
    user: User
    raw_token: Union[str, None]