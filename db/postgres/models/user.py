from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=64)
    last_name = fields.CharField(max_length=64)
    address_line_1 = fields.CharField(max_length=128)
    address_line_2 = fields.CharField(max_length=128)
    post_code = fields.CharField(max_length=15)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.id
    
    class Meta:
        table="users"


UserSchema = pydantic_model_creator(User)