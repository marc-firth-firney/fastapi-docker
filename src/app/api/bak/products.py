import logging
from fastapi import APIRouter, status, HTTPException
from app.database.schemas.products import ProductResponseSchema
import os
import sys
sys.path.insert(0, '..')
from models.product import Product
from redis import StrictRedis
from redis_cache import RedisCache
from app.config.cache import cache as cache_config
router = APIRouter(prefix="/products")
log = logging.getLogger("uvicorn")

'''
|--------------------------------------------------------------------------
| Configure Redis Cache
|--------------------------------------------------------------------------
| Here we configure a simple redis cache. This cache will be used to 
| store the product list response below
| 
|
'''
client = StrictRedis(host = cache_config["redis_url"], decode_responses = cache_config["decode_responses"])
cache = RedisCache(redis_client = client)


'''
| Endpoint that returns a list of all products
| 
| @return list[ProductResponseSchema]
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