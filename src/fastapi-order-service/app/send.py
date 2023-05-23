import coloredlogs
import pika
import logging
import os

class QueueSystemInterface:

    connection = None
    channel = None
    topic = None

    def __init__(self) -> None:
        """Initiatiser"""
        pass

    def connect(self) -> object:
        """Connect to the queue system"""
        pass

    def setTopic(self, channel) -> object:
        """Set the queue topic or exchange for messages"""
        pass

    def send(self, message) -> object:
        """Send a message to the queue"""
        pass

    def close(self) -> None:
        """Close the connection to the queue system"""
        pass

class RabbitMQQueueSystem(QueueSystemInterface):

    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
    
    def connect(self) -> object:
        """Connect to the queue system"""
        credentials = pika.PlainCredentials(
            os.environ.get("RABBITMQ_DEFAULT_USER"), 
            os.environ.get("RABBITMQ_DEFAULT_PASS")
        )

        parameters = pika.ConnectionParameters(
            host = 'rabbitmq-queue', 
            port = 5672,
            virtual_host = '/',
            credentials = credentials
        )

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        return self

    def setTopic(self, topic) -> object:
        """Set the queue topic or exchange for messages"""
        self.topic = topic
        self.channel.exchange_declare(exchange=self.topic, exchange_type='fanout')
        return self

    def send(self, message) -> object:
        """Send a message to the queue"""
        self.channel.basic_publish(exchange=self.topic, routing_key='', body=message)
        self.log.info("[ PUBLISHER ] Published message to queue: %r" % message)
        return self

    def close(self) -> None:
        """Close the connection to the queue system"""
        self.connection.close()


class QueueService():
    async def sendMessage(self, message = None) -> None:
        q = RabbitMQQueueSystem()
        q.connect().setTopic('orders')
        q.send(message)
        q.close()