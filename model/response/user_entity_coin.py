from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional, Union

from model.response.meta import Meta


class UserEntity(BaseModel):
    id: UUID
    slug: str


class Coin(BaseModel):
    id: UUID
    topup_coin_id: UUID
    token: UUID
    entity_id: Optional[UUID]
    user_id: Optional[UUID]
    is_entity: bool
    is_donate: bool
    is_used: bool
    currency: str
    created_at: datetime
    updated_at: datetime


class GenerateCoin(BaseModel):
    as_entity: Union[str, None]
    topup_id: UUID
    amount: int
    currency: str
    generated: List[Coin]


class GenerateCoinOut(BaseModel):
    meta: Meta
    response: GenerateCoin


class GetAllCoin(BaseModel):
    as_entity: Union[str, None]
    data_length: int
    data: List[Coin]


class GetAllCoinOut(BaseModel):
    meta: Meta
    response: GetAllCoin


class TrackCoinOut(BaseModel):
    meta: Meta
    response: List[Coin]


class DonateCoin(BaseModel):
    as_entity: Union[str, None]
    amount: int
    currency: str
    donate_type_to: str
    donated_to: UserEntity
    my_coin_donated: List[Coin]
    donated_coin: List[Coin]


class DonateCoinOut(BaseModel):
    meta: Meta
    response: DonateCoin


class UseCoin(BaseModel):
    as_entity: Union[str, None]
    amount: int
    nominal_conversion: float
    currency: str
    used_coin: List[Coin]


class UseCoinOut(BaseModel):
    meta: Meta
    response: UseCoin
