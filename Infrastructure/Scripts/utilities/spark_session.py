from pyspark.sql import SparkSession

def create_spark(app_name="DE_Project"):

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName(app_name) \
        .getOrCreate()

    return spark