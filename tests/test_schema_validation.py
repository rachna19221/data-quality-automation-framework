import json
import requests
from jsonschema import validate

def test_user_schema():

    response = requests.get("https://dummyjson.com/users")

    users = response.json()["users"]

    with open("schemas/user_schema.json") as f:
        schema = json.load(f)

    for user in users:
        validate(instance=user, schema=schema)