import click
import pika
import os
import json
import asyncio
from models.order import Order
from tortoise import Tortoise

''' Initialize the database '''
async def connect_to_db():
    db_url=os.environ.get("DATABASE_URL")
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models.order", "models.product", "models.user"]},
    )


''' Our main process function'''
@click.command()
def process():

    # Set up credentials for RabbitMQ using the pika library
    credentials = pika.PlainCredentials(
        str(os.environ.get("RABBITMQ_DEFAULT_USER")), 
        str(os.environ.get("RABBITMQ_DEFAULT_PASS"))
    )

    # Set up connection parameters for RabbitMQ
    parameters = pika.ConnectionParameters(
        host = str(os.environ.get("RABBITMQ_DEFAULT_HOST")), 
        port = int(os.environ.get("RABBITMQ_DEFAULT_PORT")),
        virtual_host = '/',
        credentials = credentials
    )

    # Connect to RabbitMQ
    connection = pika.BlockingConnection(parameters)

    # Create a channel
    channel = connection.channel()

    # Declare an exchange
    channel.exchange_declare(exchange = 'orders', exchange_type = 'fanout')

    # Declare a queue
    result = channel.queue_declare(queue = '', exclusive = True)

    # Get the queue's name
    queue_name = result.method.queue

    # Bind the queue to an exchange
    channel.queue_bind(exchange = 'orders', queue = queue_name)

    print(' [*] Waiting for orders. To exit press CTRL+C')

    async def ship_order(order_id: int):
        ''' Update an order status to shipped. '''
        
        # Connect to the database
        await connect_to_db()

        # Get the order and update the shipping status
        my_order = await Order.get(id=order_id)
        my_order.shipped = True
        await my_order.save()

        # Successfully shipped!
        print(f" [x] Order id #{order_id} shipped successfully!")


    def callback(ch, method, properties, body):
        ''' Callback function for the queue that executes when a message is received. '''
        
        # Decode the message as we need to extract the order id
        json_body = json.loads(body)

        # Print a message to the console so that we can see what's happening
        print(f" [x] Preparing order id #{json_body['id']}")

        # Run a background task to update the order status to shipped
        # asyncio.run(ship_order(json_body['id']))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(ship_order(json_body['id']))

        print(f" [x] Closing the order #{json_body['id']}")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    # Set up the consumer and register the callback function
    channel.basic_consume(
        queue = queue_name, 
        on_message_callback = callback, 
        auto_ack = False # auto acknowledge the message
    )

    # Start the consumer
    channel.start_consuming()

if __name__ == '__main__':
    process()