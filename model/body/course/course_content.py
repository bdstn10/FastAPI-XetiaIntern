from pydantic import BaseModel, HttpUrl, validator, ValidationError
from typing import Optional


class BaseCourseChapter(BaseModel):
    chapter_number: int
    chapter_title: str


class BaseCourseChapterUpdate(BaseModel):
    chapter_number: Optional[int]
    chapter_title: Optional[str]


class BaseCoursePart(BaseModel):
    part_number : int
    part_title : str
    video_link : HttpUrl
    article_content : Optional[str]


class BaseCoursePartUpdate(BaseModel):
    part_number : Optional[int]
    part_title : Optional[str]
    video_link : Optional[HttpUrl]
    article_content : Optional[str]

