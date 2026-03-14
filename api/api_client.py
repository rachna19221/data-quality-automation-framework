import requests

BASE_URL = "https://dummyjson.com"

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    return response.json()