from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from models.user import User
from models.product import Product


class Order(models.Model):
    id = fields.IntField(pk=True)
    product = fields.ForeignKeyField(
        'models.Product',
        on_delete=fields.CASCADE,)
    product_quantity = fields.TextField()
    user = fields.ForeignKeyField(
        'models.User',
        on_delete=fields.CASCADE,)
    shipped = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.id
    
    async def createFromPayload(self, payload):
        user = await User.get_or_none(id=payload.user_id)
    
        if not user:
            raise Exception("User not found!")
        
        product = await Product.get_or_none(id=payload.product_id)
    
        if not product:
            raise Exception(status_code=404, detail="Product not found!")

        added_order = await self.create(
            product=product,
            product_quantity=payload.product_quantity,
            user=user)
        
        return added_order
    
    class Meta:
        table="orders"


OrderSchema = pydantic_model_creator(Order)
