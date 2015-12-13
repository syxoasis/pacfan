import sqlite3

def Insert(sql):
	con = sqlite3.connect("./db/account.db")
	con.execute(sql)
	con.commit
	return 
def Init():
    con = sqlite3.connect("./db/account.db")
    con.execute("drop table account;")
    con.execute("create table account (\
           [Id] integer primary key autoincrement,\
           [UserName] varchar(10) UNIQUE,\
           [PassWord] varchar(20) not null,\
           [RegisterTime] timestamp not null default current_timestamp);")
