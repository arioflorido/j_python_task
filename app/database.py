import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbtype = os.environ.get('dbtype', 'mysql+pymysql')
user = os.environ.get('user', 'root')
password = os.environ.get('password', 'root')
host = os.environ.get('host', 'db')
port = os.environ.get('port', 3306)
db = os.environ.get('db', 'recipe_db')

SQLALCHEMY_DATABASE_URI = f'{dbtype}://{user}:{password }@{host}:{port}/{db}'

print(SQLALCHEMY_DATABASE_URI)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
