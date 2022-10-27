from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "entities" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(125) NOT NULL,
    "slug" VARCHAR(125) NOT NULL UNIQUE,
    "type" VARCHAR(125) NOT NULL,
    "country" VARCHAR(3),
    "currency" VARCHAR(3)
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "first_name" VARCHAR(125) NOT NULL,
    "last_name" VARCHAR(125),
    "slug" VARCHAR(125) NOT NULL UNIQUE,
    "email" VARCHAR(125) NOT NULL UNIQUE,
    "country" VARCHAR(3),
    "currency" VARCHAR(3)
);
CREATE TABLE IF NOT EXISTS "user_entity_role" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "role" SMALLINT NOT NULL,
    "entity_id" UUID NOT NULL REFERENCES "entities" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_user_entity_user_id_0fe49b" UNIQUE ("user_id", "entity_id")
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
