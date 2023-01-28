import pyodbc

# Connect to the database
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=tcp:yourserver.database.windows.net,1433;'
                      'Database=;'
                      'Uid='
                      'Pwd='
                      'Encrypt=yes;'
                      'TrustServerCertificate=no;'
                      'Connection Timeout=30;')

# Create a cursor
cursor = conn.cursor()

# Execute a SELECT statement
cursor.execute("SELECT * FROM table")

# Fetch all rows
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
conn.close()