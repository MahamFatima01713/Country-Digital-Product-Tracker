import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Read the .env file
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
MYSQL_DB = os.getenv("MYSQL_DB")

# Make the full MySQL connection string
DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}/{MYSQL_DB}"
)

# Engine makes the connection to MySQL
engine = create_engine(DATABASE_URL)

# Session is used to talk to the database (add, read, update, delete)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the parent of all our tables (used in models.py)
Base = declarative_base()


# FastAPI will use this function to open and close a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





# import os
# from urllib.parse import quote_plus
# from dotenv import load_dotenv
# from sqlAlchemy import create_engine
# from sqlalchemy.orm import declarative_base,sessionmaker
# load_dotenv()
# MYSQL_HOST=os.getenv("MYSQL_
#                                                              HOST")
# MYSQL_USER=os.getenv("MYSQL_USER")
# MYSQL_PASSWROD=quote_plus(os.getenv("MYSQL_PASSWORD"))
# MYSQL_DB=os.getenv("MYSQL_DB")
# DATABASE_URL=f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}"
# engine=create_engine("DATABASE_URL")
# SessionLocal=sessionmake(autocommit=false,autoflush=false,bind=engine)
# Base=declarative_base()
# def get_db()
# db= SessionLaocal()
# try:
# yield db
# finally:
# db.close()
#  
#import os
#from urllib import quote_plus 
#from getenv import load_dotenv
#from sqlalchemy import create_engine
#from sqlalchemy.orm import delacartive_base,sessionmake
#load.dotenv()
# MYSQL_HOST=os.getenv("MYSQL_HOST")
# MYSQL_USER=os.getenv("MYSQL_USER")
# MYSQL_PASSWORD=quote_plus(os.getenv("MYSQL_PASSWORD"))
# MYSQL_DB=os.getenv("MYSQL_DB")
# DATABASE_URL=f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/DB"
# ENGINE=create_engine("DATABASE_URL")
# SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=ENGINE)
# Base=declarative_base()
# def get_db()
# db=SessionLocal()
# try:
# yield_db
# finally:
# db_clode()