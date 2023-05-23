#!/bin/sh

set -euo pipefail

echo "Waiting for postgres..."
while ! nc -z postgres-db 5432; do
    sleep 0.1
done
echo "PostgreSQL started"
echo "Starting uvicorn..."
cd /usr/src/app/
uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
exec "$@"