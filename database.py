import sqlite3

def insert_exec(sql):
	con = sqlite3.connect("./db/account.db")
	con.execute(sql)
	con.commit
	return 

