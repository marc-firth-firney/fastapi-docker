## 
## Python Base Image
## 
FROM python:3.9.21-alpine as python
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN set -ex \
	&& apk add --update --no-cache netcat-openbsd build-base
RUN pip install --upgrade pip setuptools wheel
COPY ./src/__init__.py /usr/src/__init__.py
RUN export PYTHONPATH="$PYTHONPATH:..:/usr/src:/usr/src/app:/usr/src/app/services"

## 
## Tenant API (Python)
## 
FROM python as tenant-api
WORKDIR /usr/src/app
COPY ./src/requirements.txt .
COPY ./src/behave.ini ~/
RUN pip install -r requirements.txt
COPY ./src/app /usr/src/app
COPY ./src/entrypoint.sh /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh
RUN alias ll='ls -lah --color=auto'
RUN export PYTHONPATH="$PYTHONPATH:..:/usr/src:/usr/src/app:/usr/src/app/services"
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