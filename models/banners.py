from peewee import *

from models.places import Places
from models.base import BaseModel


class Banners(BaseModel):
    photo = CharField(null=True)
    name = CharField()
    position = IntegerField(null=False)
    hide = BooleanField(default=False)
    place = ForeignKeyField(Places)

    # def __str__(self):
    #     return "User(id='%s')" % self.id

