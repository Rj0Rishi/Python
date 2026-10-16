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
print("EMP table create successfully in HR database.")
conn.commit()
conn.close()
