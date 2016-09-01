from peewee import *
import dbProxy
import BaseModel

class Account(BaseModel):
    _id = IntegerField(primary_key=True)
    name = TextField()
    type = IntegerField()
    account = TextField()
    account_salt = TextField()
    salt = TextField()
    hash = TextField()
    additional = TextField()
    category = IntegerField()
    website = TextField()
