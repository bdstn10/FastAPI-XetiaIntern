from fastapi import APIRouter

actions = APIRouter(prefix="/intro", tags=["[v1] Intro"])


@actions.get("")
async def welcome():
    """
    Say welcome message
    """

    return {
        "meta": {"code": 200, "message": "success"},
        "response": "Welcome to boilerplate",
    }
