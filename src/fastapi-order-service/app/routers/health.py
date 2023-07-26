import logging
from fastapi import APIRouter, status, HTTPException
import sys
sys.path.insert(0, '..')
from models.order import Order
from models.user import User
from models.product import Product
from app.send import QueueService
import json
from tortoise.contrib.pydantic import pydantic_queryset_creator
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/health")
log = logging.getLogger("uvicorn")



''' 
Health check

Args:
    path: The API call URL path
    status_code: The expected HTTP status code for the response

Returns:
    a list of orders
'''
@router.get(
    path = "/check", 
    status_code = status.HTTP_200_OK
)
async def healthcheck() -> JSONResponse:
    response: JSONResponse = {"status": "OK"}

    return response