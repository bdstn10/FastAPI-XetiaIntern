import logging

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.v1 import router as v1_router
from app.configs import config
from database.connection import TORTOISE_ORM

Bootstrap = FastAPI(
    debug=config.debug,
    title=config.title,
    description=config.description,
    version=config.version,
    openapi_url=config.open_api_url,
    docs_url=config.docs_url,
    redoc_url=config.redoc_url,
    terms_of_service=config.term_of_service,
    contact=config.contact,
)

# include all router
Bootstrap.include_router(v1_router)

register_tortoise(
    Bootstrap,
    config=TORTOISE_ORM,
    generate_schemas=config.env == "test",
    add_exception_handlers=True,
)


@Bootstrap.on_event("startup")
async def startup() -> None:
    # await check_permission()
    pass


if config.env in ["development", "staging", "production"]:
    import sentry_sdk
    from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
    from sentry_sdk.integrations.logging import LoggingIntegration
    from sentry_sdk.integrations.redis import RedisIntegration

    sentry_sdk.init(
        dsn=config.sentry_dsn,
        environment=config.env,
        release=config.version,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        integrations=[
            LoggingIntegration(level=logging.INFO, event_level=logging.ERROR),
            RedisIntegration(),
        ],
    )

    Bootstrap.add_middleware(SentryAsgiMiddleware)
