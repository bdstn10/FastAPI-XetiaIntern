from fastapi import Query
from pydantic.main import BaseModel

# Adding pagination models
class PaginationMeta(BaseModel):
    limit: int = 15
    page: int = 1


async def paginated(
    limit: int = Query(15, description="Pagination Limit", ge=5),
    page: int = Query(1, description="Pagination Page", gt=0),
) -> PaginationMeta:
    #check limit data type
    if not isinstance(limit, int):
        raise TypeError("Limit should valid number")
    
    if not isinstance(page, int):
        raise TypeError("Limit should valid number")

    paginate_meta = PaginationMeta(limit=limit, page=page)
    return paginate_meta

