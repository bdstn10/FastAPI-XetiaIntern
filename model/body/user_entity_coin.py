from uuid import UUID
from pydantic import BaseModel
from typing import List
from uuid import UUID

class ListCoinIn(BaseModel):
    id: List[UUID]