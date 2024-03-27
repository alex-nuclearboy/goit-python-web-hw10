#!/bin/bash

echo "Starting the Postgres container..."
docker run --name quotes-hw-postgres -p 5432:5432 -e POSTGRES_PASSWORD=aN9e94poEi -d postgres
echo "Postgres is up and running on port 5432."
