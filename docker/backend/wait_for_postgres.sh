#!/bin/bash
# wait-for-postgres.sh
# https://docs.docker.com/compose/startup-order/

# Try to connect to PostgreSQL
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

chmod +x $@
# Execute given other parameters (commands)
exec "$@"