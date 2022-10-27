from lib2to3.pgen2.token import OP
from locale import currency
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from helper.points import Currency

class BasePointMethod(BaseModel):
    #base model point

    point_name: str
    min_value: float
    currency: Currency
    is_active: bool = True
    valid_until: datetime
   

class BasePointUpdate(BaseModel):
    point_name: Optional[str]
    min_value: Optional[float]
    currency: Optional[Currency]
    is_active: Optional[bool] = None
    valid_until: Optional[datetime]

