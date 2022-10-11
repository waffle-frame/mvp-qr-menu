from peewee import *

from models.users import Users
from models.base import BaseModel


# Заведения
class Places(BaseModel):
    name = CharField()
    user = ForeignKeyField(Users, null=True)

