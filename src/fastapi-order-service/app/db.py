import logging
import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")

''' Initialize the database 

Args:
    app (FastAPI): The FastAPI application

Returns:
    None
'''
async def init_db(app: FastAPI) -> None:
    """ Initialize the database """
    log.info("Registering tortoise...")
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models.order", "models.product", "models.user"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )