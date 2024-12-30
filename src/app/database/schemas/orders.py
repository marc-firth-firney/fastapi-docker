from datetime import date
from app.database.schemas.base import OurBaseModel

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
