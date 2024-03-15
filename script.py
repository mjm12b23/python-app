from google.cloud import secretmanager

def get_secret(project_id, secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

# Example usage
project_id = "precise-line-417303"
secret_id = "secret1"
secret_value = get_secret(project_id, secret_id)
print("Secret Value:", secret_value)

get_secret(project_id, secret_id, "1")