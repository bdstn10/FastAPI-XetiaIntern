from typing import Optional
from pydantic import BaseModel


class BaseCourseAchievment(BaseModel):
    achievment_name : str
    achievment_value : str


class BaseAchievmentUpdate(BaseModel):
    achievment_name : Optional[str]
    achievment_value : Optional[str]

