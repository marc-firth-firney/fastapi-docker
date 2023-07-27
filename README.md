# fastapi-docker

## Introduction
This is our sample application for use in our Workshops. 

It comprises of a selection of example services as follows:
1. FastApi Order Service - A FastAPI Application for placing orders
1. Click Fulfilment Service - A Terminal Command for processing orders
1. Postgres DB - Where order details are stored
1. RabbitMQ - Where orders are processed in a Publisher/Consumer queue
1. Redis - Used as a product data cache

## Get started - Local development
In your terminal window:
```bash
# Clone the repository for local development
git clone git@github.com:FirneyGroup/fastapi-docker.git 

# Change directory into the project root
cd ./fastapi-docker

# Store the project root path for later use
ROOT_DIR=`pwd`

# cd into the fulfilment service and copy the env file
cd $ROOT_DIR/src/click-fulfilment-service/
cp click-fulfilment-service.env.sample click-fulfilment-service.env

# cd into the order service and copy the env file
cd $ROOT_DIR/src/fastapi-order-service/
cp fastapi-order-service.env.sample fastapi-order-service.env

# cd into the postgres service and copy the env file
cd $ROOT_DIR/db/postgres/
cp db.env.sample db.env

# cd into the rabbitmq service and copy the env file
cd $ROOT_DIR/db/rabbitmq/
cp rabbitmq.env.sample rabbitmq.env

cd $ROOT_DIR
```

## Running the solution locally
Requires `docker-compose` to be installed on your machine.
```bash
docker-compose up -d
```

## Stopping the solution
Requires `docker-compose` to be installed on your machine.
```bash
docker-compose down
```

## Testing 
### Get the postman collection to test the API endpoints
Import the file `./Public.postman_collection.json` into your Postman instance.


### Start the fulfilment service
In your terminal window:
```bash
# Change to the root directory of the project
cd $ROOT_DIR

# Run the fulfilment service using the script
./fulfil
```

### Test the API endpoints

1. Import the postman collection into Postman / Hoppscotch
1. Run the `./fulfil` Command as shown in the "Start the filfilment service" section above
1. Run the `Seeder/Seed` API call to populate the database
1. Run the `Products/List All Products` API call to see all the products in the database
1. Run the `Orders/Place Orders` API call to Place an order with the fastapi-order-service
1. Note the order output from the `./fulfil` command
1. Run the `Orders/List All Orders` API call to List all Orders in the database
1. Press CTRL+C in your terminal window to cancel the `./fulfil` service at any time
