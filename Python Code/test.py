import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=localhost;"
    "Database=AdventureWorks2022;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

print("Connected Successfully")