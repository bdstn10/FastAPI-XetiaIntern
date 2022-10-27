from decimal import Decimal
import uuid
from pydantic import BaseModel
from typing import Optional

from helper.language import Language


class BaseCourseModel(BaseModel):
    product_slug: str
    approve_status: bool = False
    title: str
    subtitle: Language
    description: str
    image: str
    category_id: str
    language: Language
    prerequisities: str
    target_learner: Optional[str]
    objectives: Optional[str]
    finish_estimated: Optional[str]
    price: Decimal

    
class BaseFaqCourse(BaseModel):
    question: str
    answer: str


class BaseFaqCourseUpdate(BaseModel):
    question: Optional[str]
    answer: Optional[str]


class BaseCourseSylabus(BaseModel):
    sylabus_title: str


class BaseCourseReview(BaseModel):
    review_id: uuid.UUID

