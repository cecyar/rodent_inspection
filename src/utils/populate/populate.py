from sqlalchemy import create_engine, update, insert, delete
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute
from flask_sqlalchemy import model

import os
os.chdir("..")
#os.chdir("src/utils")
from config import SQLALCHEMY_DATABASE_URI
from models import Inspection

engine = create_engine(SQLALCHEMY_DATABASE_URI, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()


def insert_inspection(data):
    inspection_new = Inspection(**data)
    session.add(inspection_new)
    session.commit

