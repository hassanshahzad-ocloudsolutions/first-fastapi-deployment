#Engine setup (DB connection details)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') #postgreSQL
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@localhost:3306/todoapp" #mySQL
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://","postgresql://",1)



'''creating sqlalchmey engine, that will help us in establishing connection between database and fastapi application.
SQLAlchemy is ORM(Object Relational Mapper)'''

engine = create_engine(SQLALCHEMY_DATABASE_URL)

#database session
#sessionmaker is a class factory whereas SessionLocal is class not object here, we will create its objects later 
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)


Base = declarative_base() #ensures that any class inheriting Base, is a table.