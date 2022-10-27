from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel

from model.response.meta import MetaOnly


class CourseNote(BaseModel):
    note_id : UUID
    part_id : UUID
    note_title : str
    note_content : str
    user_id : UUID
    created_at : datetime
    updated_at : datetime

    class Config:
        orm_mode = True



class CourseNoteList(MetaOnly):
    response: List[CourseNote]

    class Config:
        orm_mode = True