import os
from typing import Dict, List

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    """
    Configuration class handler for this project
    """

    # App Settings
    env: str = Field("debug", env="python_env")
    debug: bool = Field(True, env="debug")
    title: str = Field("FastAPI Skeleton", env="title")
    description: str = Field("Ready to append skeleton code", env="description")
    version: str = Field("0.0.1-Alpha", env="version")
    contact: Dict = {"email": "support@xetia.io"}
    term_of_service: str = "https://xetia.io/term-of-service"
    locale: str = Field("en", env="locale")

    # Directories
    root_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Docs URL
    open_api_url: str = (
        "/private/api.json" if not os.getenv("API_GATEWAY") else "/point/openapi.json"
    )
    docs_url: str = "/global/docs" if not os.getenv("API_GATEWAY") else "/point/docs"
    redoc_url: str = "/global/redoc" if not os.getenv("API_GATEWAY") else "/point/redoc"

    # Other Services URL
    user_service_url: str = Field(
        "https://user-staging.xetia.io/api",
        env="user_service_url",
    )
    blog_service_url: str = Field(
        "https://blog-staging.xetia.io/api",
        env="blog_service_url",
    )
    notif_service_url: str = Field(
        "https://notif-staging.xetia.io/api",
        env="notif_service_url",
    )
    product_service_url: str = Field(
        "https://api.xetia.dev/product/v1",
        env="product_service_url",
    )

    # API versioning URL
    v1_prefix: str = "/api/v1" if not os.getenv("API_GATEWAY") else "/point/v1"

    # Security
    verifier: str = Field(None, env="verifier")
    algorithm: str = Field("RS256", env="algorithm")
    origin: List = ["*"]

    # Bucket
    image_bucket: str = Field("", env="image_bucket")
    gcp_cred: str = Field("user-api.json", env="gcp_cred")
    gcp_project_id: str = Field("xetia-prod01", env="gcp_project_id")

    # IMAGE
    max_upload_size: int = Field(5242880, env="max_upload_size")  # default 5 Mb

    # Rabbit MQ message broker
    rabbit_host: str = Field("localhost", env="rabbit_host")
    rabbit_port: int = Field(5672, env="rabbit_port")
    rabbit_user: str = Field("user", env="rabbit_user")
    rabbit_pass: str = Field("user", env="rabbit_pass")

    # database
    # default connection
    db_host: str = Field("localhost", env="db_host")
    db_port: int = Field(5432, env="db_port")
    db_user: str = Field("root", env="db_user")
    db_pass: str = Field("", env="db_pass")
    db_name: str = Field("xetia", env="db_name")

    # Redis cache
    redis_url: str = Field("redis://localhost:6379/0", env="redis_url")

    # List of shcema model
    schemas: List = [
        "database.schema.user_entity",
    ]

    # sentry
    sentry_dsn: str = Field("", env="sentry_dsn")

    class Config:
        env_file = ".env"


config = Config()

gcp_os = os.path.join(config.root_dir, "secrets", config.gcp_cred)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gcp_os
