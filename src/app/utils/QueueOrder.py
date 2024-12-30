
from app.vendor.services.queue.QueueService import QueueService
import logging
import json

log = logging.getLogger("uvicorn")
class QueueOrderHelper():
    async def queue(self, queue_items: list) -> None:
        """Send a message to the queue"""
        for queue_item in queue_items:

            queue_item_json = json.dumps(dict(queue_item), indent=4, sort_keys=False, default=str)
            
            log.info("Queuing: " + queue_item_json)

            queue_service = QueueService()
            await queue_service.sendMessage(queue_item_json, 'orders')