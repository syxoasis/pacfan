#!/usr/bin/env python

import sqlite3
import database
from bottle import route
from bottle import run
from bottle import template
from bottle import get
from bottle import post
from bottle import request
from bottle import static_file


@route('/')
def server_index():
	return static_file("index.html", root='./static/')
@route('/<filename>')
def server_static(filename):
	return static_file(filename, root='./static/')
@route('/index_files/<filename>')
def server_static(filename):
	return static_file(filename,root='./static/index_files/')
@route('/register')
def do_register():

	#database.insert_exec("insert into account(id,username,nickname) values (2,'oasis15@sina.com','syx');")
	return "hello word"
@post('/login')
def do_login():
	userinfo = {'username': 'root', 'total': '7M', 'register_time': '2015-12-10 13:02:37'};
	username = request.forms.get('username')
	password = request.forms.get('password')
	userinfo['username'] = username

	#return static_file("dashboard.html",root='./static')
	return template('dashboard',username=userinfo['username'],register_time = userinfo['register_time'])
	#return 
if __name__ == '__main__':
	#cu.execute("create table account (id integer primary key autoincrement,username varchar(10) UNIQUE,nickname text NULL)")
	run(host='0.0.0.0', port=8080,debug=True)
