# hammerson-tenant-data-service-fastapi/src/app/config/prismic.py
import os

'''
|--------------------------------------------------------------------------
| Prismic API Configuration
|--------------------------------------------------------------------------
| This configuration file is used to define the connection to the Prismic
| API. Details such as repository URL and access token are fetched from
| environment variables to keep them secure and configurable.
|
'''

prismic = {

    "api": {

        # Prismic repository API URL
        "endpoint": os.getenv("PRISMIC_API_ENDPOINT"),

        # Access token for private repositories
        "access_token": os.getenv("PRISMIC_ACCESS_TOKEN"),

    },

    # "cache": {

    #     # Enable or disable caching
    #     "enabled": os.getenv("PRISMIC_CACHE_ENABLED", "false").lower() == "true",

    #     # Cache TTL in seconds (default: 300 seconds)
    #     "ttl": int(os.getenv("PRISMIC_CACHE_TTL", "300")),

    # },

    # "query": {

    #     # Default number of items per page
    #     "default_page_size": int(os.getenv("PRISMIC_DEFAULT_PAGE_SIZE", "20")),

    # },

}
