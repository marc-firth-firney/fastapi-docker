from fastapi.responses import JSONResponse
import logging
from fastapi import APIRouter, status, HTTPException
import sys
sys.path.insert(0, '..')

router = APIRouter(prefix="/health")
log = logging.getLogger("uvicorn")


''' 
| Get the health check response
| 
| @return JSONResponse
'''
@router.get(
    path="/check",
    status_code=status.HTTP_200_OK
)
async def healthCheck() -> JSONResponse:
    response: JSONResponse = {"status": "OK"}

    return response
