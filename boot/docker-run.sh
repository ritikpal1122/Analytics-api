#!/bin/bash
# This script is used to run the Docker container for the application.

source /opt/venv/bin/activate

cd /code

RUN_PORT=${RUN_PORT:-8000}
RUN_HOST=${RUN_HOST:-0.0.0.0}

# this is for gunicorn to run with uvicorn worker
gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app
