from pyspark_jobs.validation_job import validate_users_with_spark

def test_users_validation():

    result = validate_users_with_spark()

    assert result == True