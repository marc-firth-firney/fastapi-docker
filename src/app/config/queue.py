import os

'''
|--------------------------------------------------------------------------
| Queue Connection Configuration
|--------------------------------------------------------------------------
| 
| 
| 
|
'''
queue = {
    "providers": [
        "rabbitmq"
    ],
    "rabbitmq": {
        "connection": {
            "host": os.getenv("RABBITMQ_DEFAULT_HOST"),
            "port": os.getenv("RABBITMQ_DEFAULT_PORT"),
            "vhost": os.getenv("RABBITMQ_DEFAULT_VHOST"),
            "username": os.getenv("RABBITMQ_DEFAULT_USER"),
            "password": os.getenv("RABBITMQ_DEFAULT_PASS"),
        }
    }
}