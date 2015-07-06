#!/usr/bin/env python
# coding=utf-8
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Required

class LoginForm(Form):
    user_name = TextField('user_name', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('登陆'.decode('utf-8'))

class EditForm(Form):
    title = TextField('title', validators = [Required()])
    content = TextAreaField('entry', validators = [Required()]) 
