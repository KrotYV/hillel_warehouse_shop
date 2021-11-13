#!/usr/bin/env sh

set -o errexit
set -o nounset

echo "Run manage.py migrate"
python manage.py migrate --noinput
echo "Run server"
exec ./manage.py runserver 0.0.0.0:8001
