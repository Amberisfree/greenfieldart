#!/bin/bash

# The Vercel platform automatically runs 'pip install'

echo "BUILD START"

# make migrations & migrate
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# collect static files
python manage.py collectstatic --no-input --clear

echo "BUILD END"