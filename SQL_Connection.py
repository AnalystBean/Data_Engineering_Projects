import pyodbc


conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=tcp:yourserver.database.windows.net,1433;'
                      'Database=;'
                      'Uid='
                      'Pwd='
                      'Encrypt=yes;'
                      'TrustServerCertificate=no;'
                      'Connection Timeout=30;')

cursor = conn.cursor()

cursor.execute("SELECT * FROM table")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
