import peewee
import dbProxy


class BaseModel(peewee.Model):
    class Meta:
        database = dbProxy
