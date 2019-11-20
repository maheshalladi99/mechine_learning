import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
 
    try:
 
        con = sqlite3.connect(':memory:') #in memory database created in ram
 
        print("Connection is established: Database is created in memory")
 
    except Error:
 
        print(Error)
 
    finally:
 
        con.close()
 
sql_connection()
