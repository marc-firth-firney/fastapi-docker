from pydantic import BaseModel
from typing import Optional
from datetime import date

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class OrderPayloadSchema(OurBaseModel):
    product_id: int
    product_quantity: int
    user_id: int

class OrderResponseSchema(OurBaseModel):
    id: int
    product_id: int
    product_quantity: int
    user_id: int
    shipped: bool
    created_at: date
    updated_at: date

    def to_string(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "product_quantity": self.product_quantity,
            "user_id": self.user_id,
            "shipped": self.shipped,
            "created_at": self.created_at,
            "updated_at": self.updated_at
       }


class OrderHealthCheckSchema(OurBaseModel):
    status: str

class ProductPayloadSchema(OurBaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductResponseSchema(OurBaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    created_at: date
    updated_at: date