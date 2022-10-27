from datetime import date, datetime
from lib2to3.pytree import Base
from locale import currency
from typing import List
from urllib import response
from uuid import UUID
from helper.points import Currency, PointType

from model.body.base_entity import BaseEntity
from model.body.point_service import BasePointMethod
from model.response.meta import MetaOnly

from pydantic import BaseModel


class PointsEntityResponse(BaseModel):
    """
        Hold Point response 
    """
    point_id: UUID
    entity_id: UUID
    point_name: str
    point_slug: str
    point_type: PointType
    min_value: float
    currency: Currency
    is_active: bool
    valid_until: datetime

    class Config:
        orm_mode = True

class PointsResponseUpdate(PointsEntityResponse):
    updated_at: datetime


class AddPointResponse(MetaOnly):

    response: PointsEntityResponse


class PointUpdate(MetaOnly):
    response: PointsResponseUpdate


class PointEntityEdit(MetaOnly):

    response: PointsEntityResponse


class PointEntityDetail(MetaOnly):
    response: PointsEntityResponse

    class Config:
        orm_mode = True


class PointMethodList(MetaOnly):
    response: List[PointsEntityResponse]


    class Config:
        orm_mode = True