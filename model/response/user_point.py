from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional

from model.response.meta import Meta


class ListUserPoint(BaseModel):
    id: UUID
    token: UUID
    purchase_id: UUID
    purchase_id_usage: Optional[UUID]
    currency: str
    created_at: datetime
    updated_at: datetime
    entity_id: UUID
    point_id: UUID
    user_id: UUID

class ClaimPoint(BaseModel):
    point_earned: int
    total_purchase: float
    countable: float
    uncountable: float
    currency: str
    detail: List[ListUserPoint]

class ClaimPointOut(BaseModel):
    meta: Meta
    response: ClaimPoint

class HistoryPointList(BaseModel):
    meta: Meta
    response: List[ListUserPoint]

class TotalByEntity(BaseModel):
    entity_slug: str
    total_point: int

class TotalByEntityOut(BaseModel):
    meta: Meta
    response: TotalByEntity

class UsePoint(BaseModel):
    purchase_id_usage: UUID
    entity_slug: str
    currency: str
    amount_used: int
    nominal_conversion: float
    detail: List[ListUserPoint]

class UsePointOut(BaseModel):
    meta: Meta
    response: UsePoint