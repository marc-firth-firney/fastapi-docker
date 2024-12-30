
'''
|--------------------------------------------------------------------------
| Postgres Models
|--------------------------------------------------------------------------
| List the models that will be regsistered in the tortoise ORM below.
| These will added to the Tortoise ORM when register_tortoise is
| called in the bootstrap. 
|
'''
models = {
    "models": [
        "models.order", 
        "models.product", 
        "models.user"
    ]
}