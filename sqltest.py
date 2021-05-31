import pyodbc

driver= '{ODBC Driver 17 for SQL Server}'

server = 'need.database.windows.net'
database = 'need'
username = 'need'
password = 'bh947018!'   

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("select * from dbo.azureex$")
        #row = cursor.fetchone()
        row = cursor.fetchall()
        #while row:
        #    print (str(row[0]) + " " + str(row[1]))
        #    row = cursor.fetchone()    
        for data in row:
            print(data)