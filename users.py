#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3
from bottle import route
from bottle import run
from bottle import template
from bottle import get
from bottle import post
from bottle import request
from bottle import static_file

def signup(signupInfo):
    con = sqlite3.connect("./db/account.db")
    sql = 'insert into account(username,password) values(?,?)'
    params = [signupInfo['user'], signupInfo['pwd']]
    con.execute(sql,params)
    con.commit()
    return signupInfo['user'] + ",恭喜你注册成功，请登录"

    #return

def update():
    return

def read():
    return

def login():
    return
