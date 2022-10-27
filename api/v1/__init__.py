from fastapi import APIRouter

from api.v1.intro.welcome import actions as welcome_actions
from app.configs import config

router = APIRouter(prefix=config.v1_prefix)

router.include_router(welcome_actions)
