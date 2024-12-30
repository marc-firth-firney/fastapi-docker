# hammerson-tenant-data-service-fastapi/src/app/services/prismic/credentials.py
from app.bootstrap.log import log
from app.config import prismic as prismic_config

class PrismicCredentials(object):
    _instance = None
    api_url = str(prismic_config["api"]["endpoint"])
    access_token = str(prismic_config["api"]["access_token"])

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PrismicCredentials, cls).__new__(cls)
            # Put any initialization here.
            cls._instance.api_url = str(prismic_config["api"]["endpoint"])
            cls._instance.access_token = str(
                prismic_config["api"]["access_token"])
        return cls._instance

    def get(self):
        """Authenticate with the Sage People API to obtain an access token."""
        log.info("Credentials: Authenticate")
        return str(f"Bearer {self.access_token}" if self.access_token else ""),
