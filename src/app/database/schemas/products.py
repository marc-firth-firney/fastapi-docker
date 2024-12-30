from datetime import date
from app.database.schemas.base import OurBaseModel

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