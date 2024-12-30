class QueueSystemInterface:

    connection = None
    channel = None
    topic = None

    def __init__(self) -> None:
        """Initiatiser"""
        raise NotImplementedError("Method or function hasn't been implemented yet.")

    def connect(self) -> object:
        """Connect to the queue system"""
        raise NotImplementedError("Method or function hasn't been implemented yet.")

    def setTopic(self, channel) -> object:
        """Set the queue topic or exchange for messages"""
        raise NotImplementedError("Method or function hasn't been implemented yet.")

    def send(self, message) -> object:
        """Send a message to the queue"""
        raise NotImplementedError("Method or function hasn't been implemented yet.")

    def close(self) -> None:
        """Close the connection to the queue system"""
        raise NotImplementedError("Method or function hasn't been implemented yet.")