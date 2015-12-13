#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sqlite3
import database
import os
import sys
import users
from bottle import route
from bottle import run
from bottle import template
from bottle import get
from bottle import post
from bottle import request
from bottle import static_file

#路由入口
@route('/')
def server_index():
	return static_file("index.html", root='./static/')

#静态资源
@route('/js/<filename>')
def server_static(filename):
	return static_file(filename, root='./static/js')
@route('/js/vendor/<filename>')
def server_static(filename):
	return static_file(filename, root='./static/js/vendor')
@route('/js/foundation/<filename>')
def server_static(filename):
	return static_file(filename, root='./static/jsfoundation')
@route('/css/<filename>')
def server_static(filename):
	return static_file(filename,root='./static/css')
@route('/img/<filename>')
def server_static(filename):
	return static_file(filename,root='./static/img')

#处理用户注册
@route('/signup', method="post")
def register_user():
	signupInfo = {}
	signupInfo['user'] = request.forms.get('SignupForm[username]')
	signupInfo['pwd'] = request.forms.get('SignupForm[password]')
	signupInfo['pwdconfirm'] = request.forms.get('SignupForm[pwdconfirm]')

	signupMessage = users.signup(signupInfo)
	return template('access',message=signupMessage)

#处理用户登录
@post('/login')
def do_login():
	logininfo = {};
	logininfo['username'] = request.forms.get('LoginForm[username]')
	logininfo['password'] = request.forms.get('LoginForm[password]')
	#message = users.login(logininfo)
	#return message
	if users.login(logininfo) == True:
		return template('users',username=logininfo['username'],register_time = '2015-10-19 11:12:34')
	else:
		return template('access',message="用户名或密码错误")


	#userinfo['username'] = username

	#return template('users',userinfo)
if __name__ == '__main__':
    #database.Init()
    run(host='0.0.0.0', port=80,debug=True)
