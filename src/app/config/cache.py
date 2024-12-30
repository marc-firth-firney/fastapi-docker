import os

'''
|--------------------------------------------------------------------------
| Redis Connection Configuration
|--------------------------------------------------------------------------
| Here we configure the connection to the Redis database. The connection
| details are stored in the environment variable REDIS_URL by
| default but we can override this if needed.
|
'''
cache = {
    "providers": [
        "redis"
    ],
    "redis": {
        "connection": {
            "url": os.getenv("REDIS_URL"),
            # "port": os.getenv("RABBITMQ_DEFAULT_PORT"),
            # "vhost": os.getenv("RABBITMQ_DEFAULT_VHOST"),
            # "username": os.getenv("RABBITMQ_DEFAULT_USER"),
            # "password": os.getenv("RABBITMQ_DEFAULT_PASS"),

        },
        "decode_responses": True
    }
}
