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
    entries  = Entry.all_entries().all()
    return render_template('index.html', entries = entries) 

@app.route('/entry/<int:id>')
def entry(id):
    if id < 0:
        flash("Sorry! Con't find this entry!")
        return redirect('index')
    entry = Entry.query.filter_by(id = id).first()
    if entry == None:
        flash("Sorry! Con't find this entry!")
        return redirect('index')
    return render_template('entry.html', entry = entry)




#@app.route('login', methods = ['POST', 'GET'])
#def login():
#    pass



