# Import Modules from ORM
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

# define Base class for table class inheritance
Base = declarative_base()

# create meta data for table class inheritance
meta = MetaData()
favourite = Table('favourite', meta, Column('id', Integer, primary_key=True,
                                            autoincrement=True,
                                            unique=True, nullable=False),
                  Column('favourites', String, nullable=False))

# create a table for class state


class Favourite(Base):
    # define table name
    __tablename__ = 'favourites'
    # define column for favourite
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    favourite = Column(String(256), nullable=False)
