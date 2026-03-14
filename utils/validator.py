def check_all_users_have_id(users):

    for user in users:
        if "id" not in user:
            return False

    return True