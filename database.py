import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("mysql+pymysql://avnadmin:AVNS_R7zPpzBjoL6Nr-cDFrP@mysql-dbf90ba-saivandani7-a273.k.aivencloud.com:12909/defaultdb")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {"ssl_disabled": False}}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
