
import requests
from datetime import datetime

USERNAME = "daksh2025"  # NEW USERNAME
TOKEN = "mynewsecrettoken"  # NEW TOKEN
GRAPH_ID = "graph1"

# Step 1: Create new user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print("--- User creation response ---")
print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print("--- Graph creation response ---")
print(response.text)

pixel_creation_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# Get today's date in YYYYMMDD format
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": "20250615" ,  # Today's date
    "quantity": "9.79",  # Your cycling distance in km
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print("--- Pixel creation response ---")
print(response.text)