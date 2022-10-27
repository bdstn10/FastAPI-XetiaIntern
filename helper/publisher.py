import json
import logging
from typing import Optional
from uuid import UUID

import pika
from app.configs import config

# Get an instance of a logger
logger = logging.getLogger("main")

# Create UUID encoder to handle UUID format
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class Publisher:
    # pika authentication credential
    crendentials = pika.PlainCredentials(
        username=config.rabbit_user, password=config.rabbit_pass
    )

    # pika connections parameter
    parameters = pika.ConnectionParameters(
        host=config.rabbit_host,
        port=config.rabbit_port,
        virtual_host=f"/{config.env}",
        credentials=crendentials,
    )

    notify_exchange = "notify"

    channel = None

    @classmethod
    def get_channel(cls):
        if cls.channel is None:
            connection = pika.BlockingConnection(cls.parameters)
            channel = connection.channel()
            return channel
        return cls.channel

    @classmethod
    async def publish(
        cls,
        exchange: str,
        body: dict,
        routing_key: Optional[str] = "",
        properties: Optional[pika.BasicProperties] = None,
        mandatory: bool = False,
    ) -> None:
        try:
            channel = cls.get_channel()

            channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=json.dumps(body, cls=UUIDEncoder),
                properties=properties,
                mandatory=mandatory,
            )

            channel.connection.close()
            logger.info("Successfully published a message!")
        except Exception as err:
            logger.exception(f"Rabbitmq publisher error. err {err.args}")

    @classmethod
    async def notify_users(
        cls,
        users: list,
        template: Optional[str] = None,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        title: Optional[str] = None,
        message: Optional[str] = None,
    ) -> None:
        exchange = cls.notify_exchange
        body = {
            "command": "notify_users",
            "users": users,
            "template": template,
            "params": params,
            "data": data,
            "title": title,
            "message": message,
        }

        await cls.publish(exchange=exchange, body=body)

    @classmethod
    async def notify_entity(
        cls,
        entity: str,
        template: str = None,
        params: dict = None,
        data: dict = None,
        title: str = None,
        message: str = None,
    ) -> None:
        exchange = cls.notify_exchange
        body = {
            "command": "notify_entity",
            "users": entity,
            "template": template,
            "params": params,
            "data": data,
            "title": title,
            "message": message,
        }

        await cls.publish(exchange=exchange, body=body)

    @classmethod
    async def notify_entity_type(
        cls,
        entity_type: list,
        template: str = None,
        params: dict = None,
        data: dict = None,
        title: str = None,
        message: str = None,
    ) -> None:
        exchange = cls.notify_exchange
        body = {
            "command": "notify_entity_type",
            "entity_type": entity_type,
            "template": template,
            "params": params,
            "data": data,
            "title": title,
            "message": message,
        }

        await cls.publish(exchange=exchange, body=body)
