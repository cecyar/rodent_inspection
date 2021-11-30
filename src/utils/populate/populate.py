from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.pool import NullPool
from sqlalchemy import insert
from sqlalchemy import delete
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute

from flask_sqlalchemy import model

engine = create_engine(SQLALCHEMY_DATABASE_URI, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()


def insert_inspection(data):
    inspection_new=Inspection(**data)
    session.add(inspection_new)
    session.commit

