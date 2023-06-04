#!/bin/bash

VERSION=0.44.3
base_github_url="https://raw.githubusercontent.com/airbytehq/airbyte-platform/v$VERSION/"
dot_env=".env"
airbyte_folder="/home/ddp/airbyte"

# Download .env file
curl -o $airbyte_folder/$dot_env $base_github_url$dot_env

secret=$(aws secretsmanager get-secret-value --secret-id dbsecrets --query SecretString --output text)
secret=$(echo $secret | sed 's/\\/\\\\/g')

database=$(echo $secret | jq -r '.[4].database')
username=$(echo $secret | jq -r '.[4].username')
password=$(echo $secret | jq -r '.[4].password')

# Set the variables in your .env file
sed -i "s/^CONFIG_DATABASE_USER=.*/CONFIG_DATABASE_USER=$username/" $airbyte_folder/$dot_env
sed -i "s/^CONFIG_DATABASE_PASSWORD=.*/CONFIG_DATABASE_PASSWORD=$password/" $airbyte_folder/$dot_env
sed -i "s/^CONFIG_DATABASE_URL=.*/CONFIG_DATABASE_URL=$database/" $airbyte_folder/$dot_env