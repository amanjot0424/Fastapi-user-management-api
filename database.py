from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
Database_URL=os.getenv("Database_URL")
engine=create_engine(Database_URL)
class Base(DeclarativeBase):
    pass

sessionlocal=sessionmaker(bind=engine)

def get_db():
    db= sessionlocal()
    try:
        yield db
    finally:
        db.close()