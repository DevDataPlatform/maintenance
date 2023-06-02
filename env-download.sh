#!/bin/bash

VERSION=0.44.3
base_github_url="https://raw.githubusercontent.com/airbytehq/airbyte-platform/v$VERSION/"
dot_env=".env"
airbyte_folder="/home/ddp/airbyte"

# Download .env file
curl -o $airbyte_folder/$dot_env $base_github_url$dot_env