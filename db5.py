import sqlite3

 
con = sqlite3.connect('D:\\mydatabase.db')
 
def sql_delete(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('Delete from employees where id = 1')
    
 
    con.commit()
 
sql_delete(con)
