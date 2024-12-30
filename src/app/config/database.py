import os

'''
|--------------------------------------------------------------------------
| Postgres Database Configuration
|--------------------------------------------------------------------------
| Set the Postgres database configuration string. This is brought in 
| using an environment variable called DATABASE_URL by default. You 
| can also specify whether or not to generate the schemas.
|
'''
database = {
    "url": os.environ.get("DATABASE_URL"),
    "tortoise": {
        "generate_schemas": True,
    }
}