import functions_framework
from google.cloud import secretmanager

@functions_framework.http
def hello_secret(request):
  # Set variables
  project_id = 'precise-line-417303' #Fill in your project
  secret_id = 'secret1'
  version_id = '1'  
  
  # Create Sercet Version Reference
  name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

  # Instantiate Secret Manager Client
  client = secretmanager.SecretManagerServiceClient()
  
  # Get Response
  response = client.access_secret_version(request={"name": name})

  # Extract 'Plain Text' Key
  secret_key = response.payload.data.decode("UTF-8")

  return 'Hello you successfully called a key from Secret Manager: {}!'.format(secret_key)
