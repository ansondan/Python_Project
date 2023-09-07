import sqlalchemy
import pandas as pd
from sqlalchemy import text

# Create a SQLAlchemy engine
password = "D#song81"
database_name = "Personal"
engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://Daniel:{password}@127.0.0.1:3306/{database_name}')

# Wrap the SQL query in a sqlalchemy.text() object
sql_query = text('SELECT * FROM Customs')

# Read the data into a Pandas DataFrame
df = pd.read_sql(sql_query, engine)

# Print the DataFrame to the console
print(df.head())
