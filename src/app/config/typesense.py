import os

'''
|--------------------------------------------------------------------------
| Typesense Configuration
|--------------------------------------------------------------------------
| This configuration file is used to define the connection to a self-hosted
| Typesense server. Details such as server URL, API key, and other options
| are fetched from environment variables to ensure security and flexibility.
|
'''

typesense = {
    "server": {
        "url": os.getenv("TYPESENSE_SERVER_URL"),  # Typesense server URL
        "api_key": os.getenv("TYPESENSE_API_KEY"),  # API key for secure access
    },
    # "connection": {
    #     "timeout": int(os.getenv("TYPESENSE_CONNECTION_TIMEOUT", "10")),  # Connection timeout in seconds (default: 10 seconds)
    #     "retry_interval": int(os.getenv("TYPESENSE_RETRY_INTERVAL", "5")),  # Retry interval in seconds (default: 5 seconds)
    # },
    # "collections": {
    #     "default_schema": os.getenv("TYPESENSE_DEFAULT_SCHEMA", "default"),  # Default schema for collections
    # },
}
