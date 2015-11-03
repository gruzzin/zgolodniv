# coding: utf-8

from zgolodniv import db
from flask.ext.security import UserMixin, RoleMixin


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    def __unicode__(self):
        return self.name


class User(db.Document, UserMixin):

    # _role_user = Role.objects.get(name='user')

    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role))
    confirmed_at = db.DateTimeField()

    def __unicode__(self):
        return self.email


class Product(db.Document):

    name = db.StringField(unique=True)
    tags = db.ListField()
    measure = db.StringField()
    meat = db.BooleanField()


class Stage(db.Document):

    text = db.StringField()
    products = db.DictField()
    image = db.StringField()


class Recipie(db.Document):

    name = db.StringField()
    preamble = db.StringField()
    stages = db.ListField(db.ReferenceField(Stage))
