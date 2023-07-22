## 
## Python Base Image
## 
FROM python:3.9.6-alpine as python
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN set -ex \
	  && apk add --update --no-cache netcat-openbsd build-base postgresql
RUN pip install --upgrade pip setuptools wheel
COPY ./db/postgres/models /usr/src/models
COPY ./src/__init__.py /usr/src/__init__.py
RUN export PYTHONPATH="$PYTHONPATH:..:/usr/src"

## 
## Fast API Order (Python)
## 
FROM python as fastapi-order
COPY ./src/fastapi-order-service/requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/fastapi-order-service/entrypoint.sh /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]


## 
## Fast API Fulfilment (Python)
## 
FROM python as click-fulfilment
COPY ./src/click-fulfilment-service/requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/click-fulfilment-service/entrypoint.sh /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]


##
## NGINX
##
FROM nginx:1.21.6-alpine as nginx
COPY nginx/conf.d /etc/nginx/conf.d
COPY nginx/nginx-entrypoint.sh /usr/local/bin/nginx-entrypoint.sh
RUN chmod +x /usr/local/bin/nginx-entrypoint*
ENTRYPOINT ["/usr/local/bin/nginx-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

##
## PubSub
##
# FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:alpine
# RUN apk --update add openjdk7-jre
# RUN gcloud components install app-engine-java kubectl
# gcloud beta emulators pubsub start --project=myproject
# gcloud beta emulators pubsub topics create orders
# gcloud beta emulators pubsub subscriptions create fulfilment-sub --topic=orders