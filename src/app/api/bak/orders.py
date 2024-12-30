from tortoise.expressions import Q
from models.product import Product
from models.user import User
from models.order import Order
import logging
from fastapi import APIRouter, status, HTTPException
from app.helpers.QueueOrder import QueueOrderHelper
from app.database.schemas.orders import OrderPayloadSchema, OrderResponseSchema
from fastapi.responses import JSONResponse
import sys
sys.path.insert(0, '..')

router = APIRouter(prefix="/orders")
log = logging.getLogger("uvicorn")


'''
| Endpoint to create an order
| 
| @param  payload  OrderPayloadSchema - The Order payload
| @return OrderResponseSchema - The added order
'''
@router.post(
    path="/",
    response_model=OrderResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_order(payload: OrderPayloadSchema) -> OrderResponseSchema:

    # log.info(f"Creating order with payload: {payload}")

    added_order: OrderResponseSchema = await Order.createFromPayload(Order, payload)

    if not added_order:
        raise HTTPException(
            status_code=500, detail="Order could not be created!")

    await queue_unfulfilled_orders()

    return added_order


'''
| Add all the unfulfilled orders to the queue
| 
| @return void
'''
async def queue_unfulfilled_orders() -> None:
    # Queue the unfulfilled orders (including any old ones that didn't previously get shipped)
    unfulfilled_orders = await Order.filter(Q(shipped=False))
    await QueueOrderHelper().queue(unfulfilled_orders)


'''
| Endpoint to list all orders
| 
| @return list[OrderResponseSchema]
'''
@router.get(
    path="/all",
    response_model=list[OrderResponseSchema],
    status_code=status.HTTP_200_OK
)
async def list_orders() -> list[OrderResponseSchema]:

    orders = await Order.all().order_by('-id')

    if not orders:
        raise HTTPException(status_code=404, detail="Order not found!")

    return orders



''' 
| Truncate and reset the sequence of the orders table
| 
| @return JSONResponse
'''
@router.get(
    path = "/truncate", 
    status_code = status.HTTP_200_OK
)
async def truncate() -> JSONResponse:
    
    await Order.raw("TRUNCATE TABLE orders RESTART IDENTITY;")

    response: JSONResponse = {"status": "Success: TRUNCATE and RESTART IDENTITY operation completed."}

    return response