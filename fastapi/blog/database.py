# what is this use for 
# this is used to create the database connection and session
# it is like a connection to the database

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL , connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine , autocommit=False , autoflush=False)

Base = declarative_base()
