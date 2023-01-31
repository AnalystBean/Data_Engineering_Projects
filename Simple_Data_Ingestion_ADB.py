import pyodbc
import pandas as pd

# Establish a connection to the Azure database
server = 'your_server_name.database.windows.net'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Read the data from a CSV file
df = pd.read_csv("data.csv")

# Insert the data into the Azure database
for index, row in df.iterrows():
    cursor.execute("INSERT INTO data_table (column_1, column_2, column_3) VALUES (?,?,?)", row['column_1'], row['column_2'], row['column_3'])

# Commit the changes and close the connection
cnxn.commit()
cursor.close()
cnxn.close()