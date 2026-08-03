import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("mysql+pymysql://avnadmin:AVNS_R7zPpzBjoL6Nr-cDFrP@mysql-dbf90ba-saivandani7-a273.k.aivencloud.com:12909/defaultdb")

print("DATABASE_URL:", DATABASE_URL)   # Temporary for debugging

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
