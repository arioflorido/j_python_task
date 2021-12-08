import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use default conn string for development purposes only.
DATABASE_URL = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:root@localhost:3306/recipe_db')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
