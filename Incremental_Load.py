
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Incremental Load Example") \
    .getOrCreate()

# Define the schema for the new data (assuming it's a DataFrame)
# Replace with your actual schema
new_data_schema = StructType([
    StructField("step", StringType()),
    StructField("type", StringType()),
    StructField("amount", StringType()),
    StructField("nameorig", StringType()),
    StructField("oldbalanceorg", StringType()),
    StructField("newbalanceorig", StringType()),
    StructField("namedest", StringType()),
    StructField("oldbalancedest", StringType()),
    StructField("newbalancedest", StringType()),
    StructField("isfraud", StringType()),
    StructField("isflaggedfraud", StringType()),
    StructField("row_id", StringType()),

])

# Load the new data into a DataFrame (replace with your actual loading logic)
# Assuming new_data_df contains the new data to be appended
new_data_df = frauddetection.filter("rowid > (SELECT MAX(rowid) FROM fraudproject)").show()

# Load the existing data from the table into a DataFrame
existing_data_df = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb") \
    .option("dbtable", "frauddetection") \
    .option("user", "consultants") \
    .option("password", "WelcomeItc@2022") \
    .load()

# Identify new records based on a unique identifier (e.g., timestamp or ID)
# In this example, we'll assume there's a 'timestamp' column for comparison
# Adjust this condition based on your specific use case
new_records_df = new_data_df.join(existing_data_df, 'rowid', 'leftanti')

# Append the new records to the existing table
new_records_df.write.format("jdbc") \
    .option("url", "jdbc:mysql://your_database_server/your_database") \
    .option("dbtable", "your_existing_table") \
    .option("user", "your_username") \
    .option("password", "your_password") \
    .mode("append") \
    .save()


# Stop the Spark session
spark.stop()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb") \
    .option("dbtable", "fraudtable") \
    .option("user", "consultants") \
    .option("password", "WelcomeItc@2022") \
    .option("driver", "org.postgresql.Driver") \
    .load()
