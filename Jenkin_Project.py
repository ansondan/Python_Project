
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .master("local") \
    .enableHiveSupport().getOrCreate()
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb") \
    .option("dbtable", "fraudtable") \
    .option("user", "consultants") \
    .option("password", "WelcomeItc@2022") \
    .option("driver", "org.postgresql.Driver") \
    .load()


df.show()