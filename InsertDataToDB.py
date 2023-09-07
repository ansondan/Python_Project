import sqlalchemy
import pandas as pd

connection_string = "mysql+mysqlconnector://Daniel:D#song81@localhost:3306/Personal"

engine = sqlalchemy.create_engine(connection_string)

# Step 3: Create a DataFrame
data = {'EmployeeID': [0, 0, 0],
        'FirstName': ['Alice', 'Bob', 'Jack']}

df = pd.DataFrame(data)

# Step 4: Insert data into the database
table_name = 'employee'

with engine.begin() as conn:
    df.to_sql(table_name, conn, if_exists='append', index=False)