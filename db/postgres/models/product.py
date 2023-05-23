from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64, unique=True)
    description = fields.TextField(default='')
    price = fields.TextField(default=0)
    stock = fields.TextField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        table="products"


ProductSchema = pydantic_model_creator(Product)