from uuid import UUID
from pydantic import BaseModel
from typing import List
from uuid import UUID

class UsePointIn(BaseModel):
    id: List[UUID]
