#!/usr/bin/env python
# coding=utf-8
from flask import (abort, flash, Markup, redirect, render_template,request,
                   Response, session, url_for)
#from flask.ext.login import login_user, logout_user, current_user, login_required
from models import Entry
from datetime import datetime, timedelta
from app import app, db

@app.route('/')
@app.route('/index')
@app.route('/blog')
def index():
    #entries  = Entry.all_entries().all()
    entries = []
    ti = 'title '
    body = 'body '
    time = datetime.now()
    for i in range(5):
        e = Entry(title = ti+str(i), content = body +str(i),
                 pub_date = time + timedelta(seconds = i))
        entries.append(e)
    return render_template('index.html', entries = entries) 

#@app.route('login', methods = ['POST', 'GET'])
#def login():
#    pass



