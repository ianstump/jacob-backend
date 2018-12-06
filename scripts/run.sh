#!/bin/bash
python manage.py migrate
python manage.py loaddata ./fixtures/db.json
python manage.py collectstatic --noinput
python manage.py search_index --rebuild
python manage.py runserver 0.0.0.0:8000
