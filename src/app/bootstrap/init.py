import logging
from fastapi import FastAPI
from app.bootstrap.db import init_db
import app.bootstrap.routers as routers
import asyncio
from app.config.meta import meta
from app.middleware.ProcessTime import ProcessTimeMiddleware
# from starlette.middleware.base import BaseHTTPMiddleware

'''
|--------------------------------------------------------------------------
| Configure Logging
|--------------------------------------------------------------------------
| Here we set up the logging using the uvicorn logger. This will ensure
| that the logs are written to STDOUT. These logs should be collected 
| by a log monitor in a scaled Production environment.
|
'''
log = logging.getLogger("uvicorn")


'''
|--------------------------------------------------------------------------
| Register The Global App Instance
|--------------------------------------------------------------------------
| To ensure that we can access the global app instance in other parts of
| the application, we register it here. This will ensure that we can
| access it to register additional routes, etc.
|
'''
global app


'''
|--------------------------------------------------------------------------
| Initialize The App Instance
|--------------------------------------------------------------------------
| Here we initialise the FastAPI instance. We als pass in some additional
| parameters that will be passed to the FastAPI instance to enable it
| to automatically generate documentation with meta information.
|
'''
app = FastAPI(
    openapi_url=meta['openapi_url'],
    docs_url=meta['docs_url'],
    title=meta["title"],
    description=meta["description"],
    summary=meta["summary"],
    version=meta["version"],
    contact={
        "name": meta["contact"]["name"],
        "url": meta["contact"]["url"],
        "email": meta["contact"]["email"],
    },
    license_info={
        "name": meta["license_info"]["name"],
        "url": meta["license_info"]["url"],
    }
)


'''
|--------------------------------------------------------------------------
| Register All The Middlewares
|--------------------------------------------------------------------------
| Here we register all the middlewares that will be used by the FastAPI
| application. These middlewares can be used to add custom 
| functionality after the request/before the response.
|
'''
middleware = ProcessTimeMiddleware(header_key="X-Process-Time")
# app.add_middleware(BaseHTTPMiddleware, dispatch=middleware)


'''
| Load All The Routers
| 
| @return void
'''
def run():
    routers.load_all()


'''
| Add an listener to the startup event
| 
| @return void
'''
# @app.on_event("startup")
# async def startup_event():
#     db_startup = init_db(app)
#     log.info("Starting Database.")
#     await asyncio.wait_for(db_startup, timeout=None)
#     log.info("Started Database.")
