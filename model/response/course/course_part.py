from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel

from model.response.meta import MetaOnly


class CoursePart(BaseModel):
    part_id : UUID
    chapter_id : UUID
    part_number : str
    video_link : str
    article_content : str
    created_at : datetime
    updated_at : datetime

    class Config:
        orm_mode = True

    
class AddCoursePart(MetaOnly):
    response : CoursePart

    class Config:
        orm_mode = True


class CoursePartList(MetaOnly):
    response : List[CoursePart]