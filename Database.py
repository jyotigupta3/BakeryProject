import sqlite3

# Connected to sqlite3
db = sqlite3.connect("Registration")

# Created cursor from database Registration
rs = db.cursor()

# Creating table name Register
rs.execute('''create table Register(name varchar(50), email varchar(100), passwd varchar(10))''')
db.commit()