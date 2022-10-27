from datetime import datetime
from lib2to3.pytree import Base
from urllib import response
from uuid import UUID
from pydantic.main import BaseModel
from decimal import Decimal
from typing import List, Optional

from tortoise.fields.data import DatetimeField

from helper.coin_status import TopUpStatus
from helper.points import Currency
from model.body.coin_service import BaseCoinModel
from model.response.meta import MetaOnly, Meta


class TopUpResponse(BaseModel):
    id: UUID
    user_id: UUID
    is_entity: bool
    entity_id: Optional[UUID]
    currency: Currency
    amount: Decimal
    transfer_fee: Decimal
    status: TopUpStatus
    created_at: datetime

    class Config:
        orm_mode = True


class TopUpStatusResponse(BaseModel):
    topup_id: UUID
    status: TopUpStatus

class AddTopUpResponse(BaseModel):
    meta: Meta
    response: TopUpResponse

class CheckTopUpStatus(BaseModel):
    meta: Meta
    response: TopUpStatusResponse

class TopUpResponseDetail(MetaOnly):
    response: TopUpResponse

    class Config:
        orm_mode = True


class TopUpResponseList(MetaOnly):
    response: List[TopUpResponse]

    class Config:
        orm_mode = True



    

