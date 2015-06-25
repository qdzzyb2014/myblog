#!/usr/bin/env python
# coding=utf-8
import os
import unittest
from datetime import datetime, timedelta

from config import basedir
from app import app, db
from app.models import Entry

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tem.db')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_all_entries(self):
        ti= 'title '
        body = 'body '
        time = datetime.now()
        for i in range(5):
            e = Entry(title = ti+str(i), content = body+str(i), 
                     pub_date = time + timedelta(seconds = i))
            db.session.add(e)

        db.session.commit()

        entries = Entry.all_entries().all()
        for i in entries:
            print i
        assert len(entries) == 5

if __name__ == '__main__':
    unittest.main()
