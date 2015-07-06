#!/usr/bin/env python
# coding=utf-8
from flask import (abort, g,flash, Markup, redirect, render_template,request, Response, session, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required
from form import LoginForm, EditForm
from models import Entry, User
from datetime import datetime, timedelta
from app import app, db, lm

@lm.user_loader
def load_user(user_name):
    return User.query.get(user_name)


@app.route('/')
@app.route('/index')
@app.route('/blog')
def index():
    entries  = Entry.all_entries().all()
    return render_template('index.html', entries = entries) 

@app.route('/entry/<int:id>', methods = ['GET', 'POST'])
def entry(id):
    if id < 0:
        flash("Sorry! Con't find this entry!")
        return redirect('index')
    entry = Entry.query.filter_by(id = id).first()
    if entry == None:
        flash("Sorry! Con't find this entry!")
        return redirect('index')

    return render_template('entry.html', entry = entry)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'),
                                request.form.get('password'))
        if user:
            login_user(user)
            flash('welcome!')
            return redirect(url_for('index'))
        else:
            flash('error')
            return redirect('/login')

    return render_template('login.html',form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Log out")
    return redirect(url_for('index'))

@app.route('/publish', methods = ['GET', 'POST'])
@login_required
def publish():
    form = EditForm()
    if form.validate_on_submit():
        entry = Entry(title = form.title.data, 
                     content = form.content.data,
                     pub_date = datetime.now())
        try:
            db.session.add(entry)
            db.session.commit()
        except:
            flash('Database error!')
            return redirect('/edit')
        flash('Publich success!')
        return redirect('/entry/%d'%(entry.id))
    return render_template('publish.html',form = form)

@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
@login_required
def edit(id):
    entry = Entry.query.filter_by(id = id).first()
    if entry == None:
        flash('entry error')
        return redirect(url_for('index'))
    form = EditForm(obj = entry)

    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        entry.pub_date = datetime.now()
        try:
            db.session.add(entry)
            db.session.commit()
        except:
            flash('Database error!')
            return redirect('/edit/%d'%entry.id)
        flash('Edit success!')
        return redirect('/entry/%d'%(entry.id))

    return render_template('publish.html', form = form)

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    entry = Entry.query.filter_by(id = id).first()
    db.session.delete(entry)
    db.session.commit()
    return redirect('/index')
