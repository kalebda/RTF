#!/bin/bash

# TODO: 
#  Add wait for postgres connection 
#  https://stackoverflow.com/questions/35069027/docker-wait-for-postgresql-to-be-running

sleep 10 # temporay wait for db connection , TODO: Replace with wait script

# alembic upgrade head

# python  setup_authO.py

#celery -A src.worker.celery_app worker -c 5 --loglevel=info &
