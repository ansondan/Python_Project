
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.functions import avg

python_executable = r"C:\Users\Consultant\AppData\Local\Programs\Python\Python311\python.exe"
os.environ["PYSPARK_PYTHON"] = python_executable
# Create a Spark session
spark = SparkSession.builder.appName("sample_data").getOrCreate()

# Read a text file
df = spark.read.csv(r"C:\Users\Consultant\Downloads\sample_data.csv", header=True, inferSchema=True)
df.show()

selected_df = df.select("Name", "Age")
selected_df.show()

df_filter = df.filter(df.Age > 30)
df_filter.show()



new_df = df.withColumn("NewSalary", col("Salary") + 10000)
new_df.show()

result_df = df.groupBy("Age").agg(avg("Salary").alias("AverageSalary"))
result_df.show()

sorted_df = df.orderBy("Age")
sorted_df.show()

df_with_condition = df.withColumn("ConditionalColumn", when(col("Age") > 30, "Yes").otherwise("No"))

# Show the DataFrame with the new column
df_with_condition.show()

df_without_salary = df.drop("Salary")

# Show the DataFrame without the "Salary" column
df_without_salary.show()

df_renamed = df.withColumnRenamed("Name", "Full Name")

# Show the DataFrame with the renamed column
df_renamed.show()

df2 = spark.createDataFrame([("Mike", 40, 80000)], ["Name", "Age", "Salary"])
df2.show()

unioned_df = df.union(df2)

unioned_df.show()
