
from app.send import QueueService
import logging
import json

log = logging.getLogger("uvicorn")


class RelayService():
    async def queue(self, orders: list) -> None:
        """Send a message to the queue"""
        for order in orders:

            order_json = json.dumps(dict(order), indent=4, sort_keys=False, default=str)
            
            log.info("Sending Order: " + order_json)

            queue_service = QueueService()
            await queue_service.sendMessage(order_json)