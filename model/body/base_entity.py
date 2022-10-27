from pydantic import BaseModel

class BaseEntity(BaseModel):
    entity: str

    class Config:
        orm_mode = True