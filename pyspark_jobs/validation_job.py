import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pyspark.sql import SparkSession
from api.api_client import get_users

def validate_users_with_spark():

    spark = SparkSession.builder \
        .appName("UserValidation") \
        .getOrCreate()

    response = get_users()

    users = response["users"]

    # Extract only simple fields
    cleaned_users = []

    for u in users:
        cleaned_users.append({
            "id": u.get("id"),
            "firstName": u.get("firstName"),
            "age": u.get("age"),
            "email": u.get("email")
        })

    df = spark.createDataFrame(cleaned_users)

    df.show()

    invalid_users = df.filter(df.id.isNull())

    if invalid_users.count() > 0:
        print("Invalid users found")
        spark.stop()
        return False
    else:
        print("All users valid")
        spark.stop()
    return True
 

validate_users_with_spark()