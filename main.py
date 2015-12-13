#!/usr/bin/env python
#-*- coding: utf-8 -*-


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
	user = request.forms.get('SignupForm[username]')
	pwd = request.forms.get('SignupForm[password]')
	pwdconfirm = request.forms.get('SignupForm[pwdconfirm]')
	signupMessage = "注册成功，请登录"
	return template('access',message=signupMessage)

#处理用户登录
@post('/login')
def do_login():
	userinfo = {'username': 'root', 'total': '7M', 'register_time': '2015-12-10 13:02:37'};
	username = request.forms.get('LoginForm[username]')
	password = request.forms.get('LoginForm[password]')
	userinfo['username'] = username

	return template('users',username=userinfo['username'],register_time = userinfo['register_time'])
	#return template('users',userinfo)
if __name__ == '__main__':
    #database.DBInit()
    run(host='0.0.0.0', port=80,debug=True)
