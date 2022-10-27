from urllib import response
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import List

from model.response.meta import MetaOnly


class CourseFAQResponse(BaseModel):
    faq_id: UUID
    course_id: UUID
    question: str
    answer: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CourseFAQUpdateResponse(CourseFAQResponse):
    updated_at: datetime



class AddCourseFAQResponse(MetaOnly):
    response: CourseFAQResponse



class UpdateFAQResponse(MetaOnly):
    response: CourseFAQUpdateResponse

    class Config:
        orm_mode = True


class CourseFAQDetails(MetaOnly):
    response: CourseFAQUpdateResponse

    class Config:
        orm_mode = True


class CourseFAQList(MetaOnly):
    response: List[CourseFAQResponse]

    class Config:
        orm_mode = True