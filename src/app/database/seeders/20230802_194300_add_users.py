import logging
import sys
sys.path.insert(0, '..')
from models.user import User

log = logging.getLogger("uvicorn")

'''
| Add users to the DB
| 
| @return void
'''
async def seed() -> None:
    
    log.info("Seeding users")

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

    log.info("Seeded users")
