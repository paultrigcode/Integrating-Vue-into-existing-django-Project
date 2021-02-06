#!/usr/bin/env bash
echo 'Starting python process'
# watch -n 3 "wget 0.0.0.0:8000 -O /dev/null -o /dev/null" &
echo 'yes'| python manage.py collectstatic 

/usr/local/bin/gunicorn boilertemplate.wsgi:application -w 2 -b :9000 --reload --reload-extra-file="/src/."
