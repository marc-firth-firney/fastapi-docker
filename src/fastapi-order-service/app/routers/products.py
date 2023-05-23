import logging
from fastapi import APIRouter, status, HTTPException
from app.schemas.pydantic import ProductResponseSchema
import os
import sys
sys.path.insert(0, '..')
from models.product import Product
from redis import StrictRedis
from redis_cache import RedisCache

router = APIRouter(prefix="/api/products")
log = logging.getLogger("uvicorn")

# Configure redis
client = StrictRedis(host=os.environ.get("REDIS_URL"), decode_responses=True)
cache = RedisCache(redis_client=client)


''' 
List all products

Args:
    path: The API call URL path
    status_code: The expected HTTP status code for the response

Returns:
    a list of products
'''
@cache.cache(ttl=60)
@router.get(
        path = "/all", 
        response_model = list[ProductResponseSchema], 
        status_code = status.HTTP_200_OK
)
async def list_products() -> list[ProductResponseSchema]:
    
    products = await Product.all()

    if not products:
        raise HTTPException(status_code=404, detail="Products not found!")
    
    return products