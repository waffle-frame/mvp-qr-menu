import sqlite3

from peewee import *

from datetime import datetime
from models.base import BaseModel

class Users(BaseModel):
    username = CharField()
    password = CharField()
    created_at = DateTimeField(default=datetime.now())

    