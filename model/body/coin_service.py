from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from pypika.terms import NullValue

from tortoise.fields.base import CASCADE
from helper.coin_status import TopUpStatus
from helper.points import Currency

class UserTopUp(BaseModel):
    id: uuid.UUID

class EntityTopUp(BaseModel):
    id: uuid.UUID

class BaseCoinModel(BaseModel):
    amount: Decimal
    transfer_fee: Decimal

class BaseUpdateTopUp(BaseModel):
    status: TopUpStatus

class UserCoin(BaseModel):
    is_entity: bool
    is_donated: bool = False
    is_used: bool = False
    currency = Currency

