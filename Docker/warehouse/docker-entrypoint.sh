#!/usr/bin/env sh

set -o errexit
set -o nounset

cmd="$*"

postgres_ready () {
  sh '/wait-for-command.sh' -t 5 -s 0 52 -c "curl dbwarehouse:5432"
}

until postgres_ready; do
  >&2 echo 'Postgres is unavailable - sleeping'
done

>&2 echo 'Postgres is up - continuing...'

exec $cmd