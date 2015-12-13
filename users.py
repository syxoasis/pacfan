#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3
import bcrypt
from bottle import route
from bottle import run
from bottle import template
from bottle import get
from bottle import post
from bottle import request
from bottle import static_file

def signup(signupInfo):
    hashed = bcrypt.hashpw(signupInfo['pwd'], bcrypt.gensalt())
    con = sqlite3.connect("./db/account.db")
    sql = 'insert into account(username,pwdhash) values(?,?)'
    params = [signupInfo['user'], hashed]
    try:
        con.execute(sql,params)
        con.commit()
    except Exception,ex:
        return "用户[" + signupInfo['user'] + "]已被注册"
    return signupInfo['user'] + ",恭喜你注册成功，请登录"

def login(logininfo):
    con = sqlite3.connect("./db/account.db")
    cu = con.cursor()
    sql = 'select pwdhash from account where username = ?'
    params = [logininfo['username']]
    try:
        cu.execute(sql,params)
        result = cu.fetchone()
        hashed = result[0].encode("ascii")
    except Exception,ex:
        return ex
    if bcrypt.hashpw(logininfo['password'], hashed) == hashed:
        return True
    else:
        return False

def update():
    return

def read():
    return
