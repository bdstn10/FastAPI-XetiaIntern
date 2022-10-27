from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class BaseNote(BaseModel):
    note_title : str
    note_content : str


class BaseNoteUpdate(BaseModel):
    note_title : Optional[str]
    note_content : Optional[str]

