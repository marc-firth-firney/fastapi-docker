import logging
from fastapi import APIRouter, status, HTTPException
import sys
sys.path.insert(0, '..')
from models.product import Product
from models.user import User

router = APIRouter(prefix="/api/seed")
log = logging.getLogger("uvicorn")

''' 
Seed the database 

Args:
    path: The API call URL path
    status_code: The expected HTTP status code for the response

Returns:
    JSON response
'''
@router.get(path = "/", status_code = status.HTTP_201_CREATED)
async def seed():
    
    log.info("Seeding database")
    
    await Product.get_or_create(
        name = 'Toothbrush',
        description = 'A firm toothbrush',
        price = '2.99',
        stock = '100',
    )

    await Product.get_or_create(
        name = "Umbrella",
        description = "A blue umbrella",
        price = 7.99,
        stock = 300
    )

    await Product.get_or_create(
        name = "Camping Stove",
        description = "A folding camping stove",
        price = 15.99,
        stock = 300
    )

    await User.get_or_create(
        first_name = "Mario",
        last_name = "Mario",
        address_line_1 = "1 Rainbow Road",
        address_line_2 = "The Mushroom Kingdom",
        post_code = "RA1 7BO"
    )

    await User.get_or_create(
        first_name = "Princess",
        last_name = "Peach",
        address_line_1 = "2 Rainbow Road",
        address_line_2 = "The Mushroom Kingdom",
        post_code = "RA1 7BO"
    )

    await User.get_or_create(
        first_name = "Luigi",
        last_name = "Mario",
        address_line_1 = "3 Rainbow Road",
        address_line_2 = "The Mushroom Kingdom",
        post_code = "RA1 7BO"
    )

    return {"status": "success"}