#!/usr/bin/env python
# coding=utf-8
from app import db
from hashlib import md5
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    pub_date = db.Column(db.DateTime, index = True)

    @classmethod
    def all_entries(cls):
        return cls.query.order_by(cls.pub_date.desc())

    def __repr__(self):
        return '<titile: %r> <content: %r>' % (self.title, self.content)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))
    def __repr__(self):
        return '<user_name: %r>'%(self.user_name)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def get_id(self):
        return unicode(self.id)
    def is_anonymous(self):
        return False
    
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
    
    @classmethod
    def login_check(cls, user_name, password):
        user = cls.query.filter(
            db.and_(User.user_name == user_name, User.password == password)
        ).first()
        if not user:
            return None
        return user
