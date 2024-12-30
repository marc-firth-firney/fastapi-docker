import logging
import sys
sys.path.insert(0, '..')
from models.product import Product

log = logging.getLogger("uvicorn")

'''
| Add Products to the DB
| 
| @return void
'''
async def seed():

    log.info("Seeding products")

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

    log.info("Seeded products")
