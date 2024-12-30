# import os
# from fastapi import FastAPI
# from tortoise.contrib.fastapi import register_tortoise
# from app.bootstrap.helpers import seeders_path
# from app.config.models import models
# from app.config.database import database
# import asyncio
# import gc
# import logging

# log = logging.getLogger("uvicorn")
# log.info("Starting...")

# '''
# | Initialise the database
# |
# | @param  FastAPI  app - Our FastAPI application
# | @return void
# '''
# async def init_db(app: FastAPI) -> None:
#     register_tortoise(
#         app,
#         db_url=database["url"],
#         modules=models,
#         generate_schemas=database["tortoise"]["generate_schemas"],
#         add_exception_handlers=True,
#     )

# '''
# | See the database
# |
# | @return void
# '''
# async def seed_db():
#     for path in seeders_path().glob("[!_]*.py"):
#         module_name = os.path.basename(path).replace(".py", "")
#         print(module_name)

#         dynamic_import_name = "app.database.seeders." + str(module_name)

#         # Import the module
#         # This is equivalent to:
#         # From app.database.seeders import 20230802_194300_add_users
#         dynamic_import = __import__(dynamic_import_name, fromlist=["seed"])

#         await dynamic_import.seed()
