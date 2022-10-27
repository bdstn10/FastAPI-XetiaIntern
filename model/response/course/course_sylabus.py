from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from model.response.meta import MetaOnly


class CourseSylabusResponse(BaseModel):
    sylabus_id : UUID
    course_id : UUID
    sylabus_attachment : str
    created_at: datetime
    updated_at: datetime


    class Config:
        orm_mode = True


class AddCourseSylabus(MetaOnly):
    response: CourseSylabusResponse

    class Config:
        orm_mode = True


class CourseSylabusDetail(MetaOnly):
    response: CourseSylabusResponse

    class Config:
        orm_mode = True