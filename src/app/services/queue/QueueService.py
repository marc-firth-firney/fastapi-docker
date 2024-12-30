from app.vendor.services.queue.connectors import RabbitMQQueueSystem

class QueueService():
    async def sendMessage(self, message: str = None, topic: str = None) -> None:
        """Send a message to the queue"""
        q = RabbitMQQueueSystem()  # TODO: Replace with Registry
        q.connect().setTopic(topic)
        q.send(message)
        q.close()
