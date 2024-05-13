#! /usr/bin/env sh

set -e

DEFAULT_MODULE_NAME=src.main
MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

DEFAULT_GUNICORN_CONF=/app/gunicorn_conf.py
export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
#export WORKER_CLASS=${WORKER_CLASS:-"eventlet"}
export WORKER_CLASS=${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}

# If there's a prestart.sh script in the /app directory or other path specified, run it before starting
PRE_START_PATH=${PRE_START_PATH:-/app/prestart.sh}
echo "Checking for prestart script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running prestart script $PRE_START_PATH"
    . "$PRE_START_PATH"
else 
    echo "There is no prestart script $PRE_START_PATH"
fi

# Start Gunicorn
exec gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
#exec gunicorn "$APP_MODULE" --workers 0 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
#exec gunicorn -w 1 -k $WORKER_CLASS --preload -c "$GUNICORN_CONF" "$APP_MODULE"