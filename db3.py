import sqlite3
 
#con = sqlite3.connect('D:\\db1.db')
con = sqlite3.connect('D:\\mydatabase.db') 
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()
 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
entities = (1, 'Smith', 700, 'IT', 'Tech', '2018-12-06')
sql_insert(con, entities)
