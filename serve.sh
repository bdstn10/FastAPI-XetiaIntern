#!/usr/bin/env bash

serve_type=$1

if [ -z "$1" ]
then
    echo "No type selected, default to: gunicorn"
    serve_type="gunicorn"
fi

if [ "$RUN_MIGRATION" = true ]
then
    echo "Running migration"
    aerich upgrade
fi

if [ $serve_type = "gunicorn" ]
then
    echo "Running gunicorn"
    if [ "$PYTHON_ENV" = "development" ] || [ "$PYTHON_ENV" = "staging" ] || [ "$PYTHON_ENV" = "production" ];
    then
        gunicorn -k uvicorn.workers.UvicornWorker -b unix:///dev/shm/gunicorn.sock index:app
    else
        gunicorn -k uvicorn.workers.UvicornWorker -b :"$PORT" index:app
    fi
fi

if [ $serve_type = "nginx" ]
then
    echo "Running nginx"
    nginx -g 'daemon off;'
fi
