from api.v1.point_service import router as point_router
from api.v1.user_point import point as user_point_router
from api.v1.top_up_service import topup as top_up_service
from api.v1.user_entity_coin import router as user_entity_coin_router

# course system
from api.v1.course.overview import router as course_service
from api.v1.course.course_faq import router as course_faq
from api.v1.course.course_sylabus import router as course_sylabus
from api.v1.course.course_review import router as course_review
from api.v1.course.course_chapter import router as course_chapter
from api.v1.course.course_part import course_part_router as course_part
from api.v1.course.course_quiz import quiz_router as quiz_router
from api.v1.course.course_note import router_note as course_note 
from api.v1.course.course_achievment import router_achievment as course_achievment

from fastapi import APIRouter
from app.configs import config



v1_router = APIRouter(prefix=config.v1_prefix)

v1_router.include_router(point_router)
v1_router.include_router(user_point_router)
v1_router.include_router(top_up_service)
v1_router.include_router(user_entity_coin_router)

# course system
v1_router.include_router(course_service)
v1_router.include_router(course_faq)
v1_router.include_router(course_sylabus)
v1_router.include_router(course_review)
v1_router.include_router(course_chapter)
v1_router.include_router(course_part)
v1_router.include_router(quiz_router)
v1_router.include_router(course_note)
v1_router.include_router(course_achievment)