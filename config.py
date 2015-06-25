#!/usr/bin/env python
# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True

#init superuser
SUPER_USER = "qdzzyb"
SECRET_KEY = "you-will-never-guess"
#init database
SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

