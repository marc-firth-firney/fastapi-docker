import logging
from fastapi import FastAPI
from app.routers import orders, products, seeder
from app.db import init_db

# Set up logging
log = logging.getLogger("uvicorn")
log.info("Starting...")

# Initialise the app and routes
app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs"
)
app.include_router(orders.router,tags=["order"])
app.include_router(products.router,tags=["product"])
app.include_router(seeder.router,tags=["seeder"])

@app.on_event("startup")
async def startup_event():
    await init_db(app)
