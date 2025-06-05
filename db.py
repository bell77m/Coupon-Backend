import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Example MySQL connection string:
# "mysql+pymysql://<username>:<password>@<host>/<database>"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://bell77m:12345678@localhost/coupon"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    return SessionLocal()
