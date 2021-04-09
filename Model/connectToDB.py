from peewee import *

#database = MySQLDatabase('Carsharing', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT',
#'use_unicode': True, 'user': 'root', 'password': ''})

db = SqliteDatabase('carDatabase.db', pragmas={'journal_mode': 'wal'})

class BaseModel(Model):
    class Meta:
        database = db

