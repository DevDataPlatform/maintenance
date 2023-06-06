import json
import subprocess


VERSION = "0.44.3"
base_github_url = f"https://raw.githubusercontent.com/airbytehq/airbyte-platform/v{VERSION}/"
dot_env = ".env"
airbyte_folder = "/home/ddp/airbyte"


# Download .env file
subprocess.check_output(["curl", "-o", f"{airbyte_folder}/{dot_env}", f"{base_github_url}{dot_env}"])

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
subprocess.check_output(["sed", "-i", "", "-e", f"s/^CONFIG_DATABASE_USER=.*/CONFIG_DATABASE_USER={username}/", f"{airbyte_folder}/{dot_env}"])
subprocess.check_output(["sed", "-i", "", "-e", f"s/^CONFIG_DATABASE_PASSWORD=.*/CONFIG_DATABASE_PASSWORD={password}/", f"{airbyte_folder}/{dot_env}"])
subprocess.check_output(["sed", "-i", "", "-e", f"s/^CONFIG_DATABASE_URL=.*/CONFIG_DATABASE_URL={database}/", f"{airbyte_folder}/{dot_env}"])
