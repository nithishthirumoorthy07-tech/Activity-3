#!/usr/bin/env bash
# Render build script for the Django backend.
# Render calls this file automatically when the service is deployed.
# Set it as the Build Command in your Render web service settings.

set -o errexit   # exit immediately on any error

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
