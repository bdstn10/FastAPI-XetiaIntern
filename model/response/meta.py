from pydantic import BaseModel

class Meta(BaseModel):
    code: int
    message: str


class MetaOnly(BaseModel):
    # menampilkan response dalam bentuk meta only
    meta: Meta