from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel

from model.response.meta import MetaOnly


class CourseChapter(BaseModel):
    course_id : UUID
    chapter_id : UUID
    chapter_number : str
    chapter_title : str
    created_at : datetime
    updated_at : datetime

    class Config:
        orm_mode = True

    
class AddCourseChapter(MetaOnly):
    response : CourseChapter

    class Config:
        orm_mode = True


class CourseChapterList(MetaOnly):
    response : List[CourseChapter]