import click
import logging
import pika
import os
import json
from models.order import Order

log = logging.getLogger(__name__)

@click.command()
# @click.option('--queue', prompt='Queue name',
#               help='The RabbitMQ queue name.')
# @click.option('--tries', prompt='Number of retries',
#               help='The number of retries before failing an item.')
def process():

    credentials = pika.PlainCredentials(
        os.environ.get("RABBITMQ_DEFAULT_USER"), 
        os.environ.get("RABBITMQ_DEFAULT_PASS")
    )

    parameters = pika.ConnectionParameters(
        host = 'rabbitmq-queue', 
        port = 5672,
        virtual_host = '/',
        credentials = credentials
    )

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.exchange_declare(exchange = 'orders', exchange_type = 'fanout')

    result = channel.queue_declare(queue = '', exclusive = True)

    queue_name = result.method.queue

    channel.queue_bind(exchange = 'orders', queue = queue_name)

    print(' [*] Waiting for orders. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        body = json.loads(body)
        print(f" [x] Processing order id #{body['id']}")
        order = Order.get(body['id'])
        order.shipped = True
        order.save()
        print(f" [x] Order id #{body['id']} shipped successfully!")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue = queue_name, 
        on_message_callback = callback, 
        auto_ack = False
    )

    channel.start_consuming()

if __name__ == '__main__':
    process()