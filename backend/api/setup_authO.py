import json
import sys

import requests

sys.path.insert(0, "../src")
from src.core.config import settings


def get_token_for_mgmt_api():
    url = f"https://{settings.auth0_domain}/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": f"{settings.client_id}",
        "client_secret": f"{settings.client_secret}",
        "audience": f"{settings.auth0_audience}"
        # "audience": f"https://{settings.auth0_domain}/api/v2/",
    }

    headers = {"content-type": "application/x-www-form-urlencoded"}

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["access_token"]
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.text)


# Constants for roles
ROLES = [
    {"Role": "ADMIN", "Description": "this is an admin of the app"},
    {"Role": "CLIENT", "Description": "this is the client of the app"},
]

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {get_token_for_mgmt_api()}",
}


# Function to get a list of existing roles from Auth0
def get_auth0_roles():
    url = f"https://{settings.auth0_domain}/api/v2/roles"
    response = requests.get(url, headers=headers)
    return response.json()


# Function to create a role in Auth0
def create_auth0_role(name, description):
    url = f"https://{settings.auth0_domain}/api/v2/roles"
    data = {"name": name, "description": description}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response


# Check if roles exist in Auth0, and create them if not
existing_roles = get_auth0_roles()
existing_roles_lower = [r["name"].lower() for r in existing_roles]
for role in ROLES:
    role_name = role["Role"].lower()
    role_description = role["Description"]

    if role_name not in existing_roles_lower:
        create_auth0_role(role_name, role_description)
        print(f"Created role: {role_name}")

print("Auth0 role setup completed.")

if "admin" in existing_roles_lower:
    for role in existing_roles:
        if role["name"] == "admin":
            admin_role_id = role["id"]
url = f"https://{settings.auth0_domain}/api/v2/users"

try:
    payload = json.dumps(
        {
            "email": "kalebu246@gmail.com",
            "email_verified": True,
            "name": "Kaleb",
            "password": "Test@123",
            "verify_email": False,
            "connection": "Username-Password-Authentication",
        }
    )

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 201:
        data = response.json()

        id_value = data.get("user_id")
        payload = json.dumps(
            {
                "users": [
                    id_value,
                ]
            }
        )
        url = f"https://{settings.auth0_domain}/api/v2/roles/{admin_role_id}/users"
        response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

except Exception as e:
    # Handle the exception here
    print(f"An error occurred: {e}")
