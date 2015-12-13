#!/usr/bin/env python

import sqlite3
import database
import os
import sys
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
@route('/css/<filename>')
def server_static(filename):
	return static_file(filename,root='./css')
@route('/register', method="get")
def send_form_register():
	return static_file("register.html",root='./static/')
@route('/register', method="post")
def register_user():
	user = request.forms.get('RegisterForm[username]')
	pwd = request.forms.get('RegisterForm[password]')
	#database.Insert("insert into account(username,password) values ('"+user+"','"+pwd+"');")
	return "insert into account(username,password) values ('"+user+"','"+pwd+"');"
    #return "after insert"
@post('/login')
def do_login():
	userinfo = {'username': 'root', 'total': '7M', 'register_time': '2015-12-10 13:02:37'};
	username = request.forms.get('LoginForm[username]')
	password = request.forms.get('LoginForm[password]')
	userinfo['username'] = username

	#return static_file("dashboard.html",root='./static')
	return template('dashboard',username=userinfo['username'],register_time = userinfo['register_time'])
	#return 
if __name__ == '__main__':
    #database.DBInit()
    run(host='0.0.0.0', port=80,debug=True)
