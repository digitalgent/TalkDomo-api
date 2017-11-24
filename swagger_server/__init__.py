import os
from os.path import join, dirname
from datetime import datetime
from dotenv import load_dotenv
from flask.json import JSONEncoder

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlite3 import dbapi2 as sqlite

from swagger_server.models.base import Base

# Settings
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# SQL Alchemy
engine = create_engine(os.environ.get("SQL_ENGINE"), module=sqlite, convert_unicode=True)
session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine)

db = session()

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return obj.to_dict()
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d')
        return super(CustomJSONEncoder, self).default(obj)
