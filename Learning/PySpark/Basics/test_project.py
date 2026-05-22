import sys
sys.path.append(r"D:\DE_projects")
from Infrastructure.Scripts.utilities.spark_session import create_spark
from Infrastructure.Scripts.utilities.logger import logger

# Create Spark Session
spark = create_spark("Test_Project")

logger.info("Spark Session Created")

# Create DataFrame
data = [
    (1, "Swami"),
    (2, "Spark")
]

columns = ["id", "name"]

df = spark.createDataFrame(data, columns)

# Show Data
df.show()

logger.info("Data Displayed Successfully")

spark.stop()

logger.info("Spark Session Stopped")