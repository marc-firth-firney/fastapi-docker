import logging
from fastapi import APIRouter, status, HTTPException
import sys
sys.path.insert(0, '..')
from app.bootstrap.db import seed_db
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/seed")
log = logging.getLogger("uvicorn")


'''
| Endpoint to trigger database seeding
| 
| @return JSONResponse
'''
@router.get(path = "/", status_code = status.HTTP_201_CREATED)
async def seed() -> JSONResponse:
    
    log.info("Seeding database")
    
    await seed_db()
    response: JSONResponse = {"status": "Successfully seeded the database."}

    return response