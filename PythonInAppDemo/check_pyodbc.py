"""import os
while True:
    try:
        import pyodbc
        print("pyodbc imported")
        break
    except:
        print(os.popen("pip install pyodbc").read())
        continue

print("the rest of your script here")"""


import pyodbc

print(pyodbc.drivers())
['SQL Server', 'SQL Server Native Client 11.0', 'SQL Server Native Client RDA 11.0', 'ODBC Driver 17 for SQL Server', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)']