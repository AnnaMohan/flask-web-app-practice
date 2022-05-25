from __future__ import unicode_literals
from email.policy import default
from enum import unique
from time import timezone
from unicodedata import category
from importlib_metadata import email
from . import db ## here '.' represent the current package if incase we need to use this
# db object in anothe packer that line will be as from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# inheriting Model class from database
class Note(db.Model):
    # Column is a class
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # in SqlAlchemy for foreign key we need to give the class name
    # lower case here we have given User class name as user.id to get
    # the id of the user to identify who is creating the notes.

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

print(User.email)