import sqlite3
conn = sqlite3.connect('HR.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS EMP(
Eno INTEGER PRIMARY KEY,
Ename TEXT NOT NULL,
Salary REAL
)
''')
cursor.execute("INSERT INTO EMP(Eno,Ename,Salary)VALUES(10,'Alice',50000)")
cursor.execute("INSERT INTO EMP(Eno,Ename,Salary)VALUES(30,'Jack',50000)")
cursor.execute("INSERT INTO EMP(Eno,Ename,Salary)VALUES(20,'BOb',11000)")
conn.commit()
cursor.execute("SELECT * FROM EMP")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()
