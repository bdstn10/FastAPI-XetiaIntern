from app.configs import config

if config.env == "test":
    dbname = f"{config.db_name}_test"
else:
    dbname = config.db_name

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": config.db_host,
                "port": config.db_port,
                "user": config.db_user,
                "password": config.db_pass,
                "database": dbname,
            },
        },
    },
    "apps": {
        "models": {
            "models": [*config.schemas, "aerich.models"],
            "default_connection": "default",
        },
    },
}
