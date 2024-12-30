import pika
import logging
from app.config.queue import queue as queue_config
from app.vendor.services.queue.QueueSystemInterface import QueueSystemInterface

class RabbitMQQueueSystem(QueueSystemInterface):

    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
    
    def connect(self) -> object:
        """Connect to the queue system"""
        credentials = pika.PlainCredentials(
            str(queue_config["rabbitmq"]["connection"]["username"]), 
            str(queue_config["rabbitmq"]["connection"]["password"])
        )

        parameters = pika.ConnectionParameters(
            host = str(queue_config["rabbitmq"]["connection"]["host"]), 
            port = int(queue_config["rabbitmq"]["connection"]["port"]),
            virtual_host = str(queue_config["rabbitmq"]["connection"]["vhost"]),
            credentials = credentials
        )

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        return self

    def setTopic(self, topic: str) -> object:
        """Set the queue topic or exchange for messages"""
        self.topic = topic
        self.channel.exchange_declare(exchange=self.topic, exchange_type='fanout')
        return self

    def send(self, message: str) -> object:
        """Send a message to the queue"""
        self.channel.basic_publish(exchange=self.topic, routing_key='', body=message)
        self.log.info("[ PUBLISHER ] Published message to queue: %r" % message)
        return self

    def close(self) -> None:
        """Close the connection to the queue system"""
        self.connection.close()