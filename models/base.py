from peewee import *

sqlite = SqliteDatabase(
    './db.db', 
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64
    }
)




class BaseModel(Model):
    class Meta:
        database = sqlite