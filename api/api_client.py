from utils.logger import logger
import requests

BASE_URL = "https://dummyjson.com"

def get_users():
    logger.info("Fetching users API")
    response = requests.get(f"{BASE_URL}/users")
    logger.info(f"Status code: {response.status_code}")
    response.raise_for_status()
    return response.json()