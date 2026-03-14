from api.api_client import get_users
from utils.validator import check_all_users_have_id

def test_users_have_id():

    response = get_users()

    users = response["users"]

    assert check_all_users_have_id(users)