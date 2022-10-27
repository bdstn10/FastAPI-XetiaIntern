import json
import uuid
from typing import Dict

import pika
from app.configs import config

from helper.json_encoder import UUIDSafeJsonEncoder


class RPCClient:
    """
    RPC client
    """

    def __init__(self, command: str, route_key: str):
        self.command = command
        self.route_key = route_key

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=config.rabbit_host,
                port=config.rabbit_port,
                virtual_host=f"/{config.env}",
                credentials=pika.PlainCredentials(
                    username=config.rabbit_user, password=config.rabbit_pass
                ),
            )
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_message_callback,
            auto_ack=True,
        )

    def on_message_callback(self, ch, method, props, body):
        if self.correlation_id == props.correlation_id:
            self.response = json.loads(body)

    def get_response(self, data: Dict):
        self.response = None
        self.correlation_id = str(uuid.uuid1())
        self.channel.basic_publish(
            exchange="",
            routing_key=self.route_key,
            properties=pika.BasicProperties(
                headers={"command": self.command},
                reply_to=self.callback_queue,
                correlation_id=self.correlation_id,
            ),
            body=json.dumps(data, cls=UUIDSafeJsonEncoder),
        )

        while self.response is None:
            self.connection.process_data_events()

        return self.response
