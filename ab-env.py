import os
import json
import subprocess

VERSION = "0.44.3"
base_github_url = f"https://raw.githubusercontent.com/airbytehq/airbyte-platform/v{VERSION}/"
dot_env = ".env"
airbyte_folder = "/home/ddp/airbyte"


# Download .env file
os.system(f"curl -o {airbyte_folder}/{dot_env} {base_github_url}{dot_env}")

secret = subprocess.check_output(['aws', 'secretsmanager', 'get-secret-value', '--secret-id', 'dbsecrets', '--query', 'SecretString', '--output', 'text'])
secret = secret.decode()
secret = secret.replace("'", "\"")
secret = json.loads(secret) 

database = None
password = None
username = None

for item in secret:
    if item['database'] == 'airbyte-configdb':
        database = item['database']
        username = item['username']
        password = item['password']
        break


# Set the variables in your .env file
os.system(f"sed -i '' -e 's/^CONFIG_DATABASE_USER=.*/CONFIG_DATABASE_USER={username}/' {airbyte_folder}/{dot_env}")
os.system(f"sed -i '' -e 's/^CONFIG_DATABASE_PASSWORD=.*/CONFIG_DATABASE_PASSWORD={password}/' {airbyte_folder}/{dot_env}")
os.system(f"sed -i '' -e 's/^CONFIG_DATABASE_URL=.*/CONFIG_DATABASE_URL={database}/' {airbyte_folder}/{dot_env}")
