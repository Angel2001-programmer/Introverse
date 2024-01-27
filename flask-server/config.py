from dotenv import load_dotenv  # dotenv vs decouple
import os
import redis
# from mysqlconfig import HOST, USER, PASSWORD

load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
database = os.getenv("DATABASE")

# MySQL database connection
mysql_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# For SQLite DB
sqlite_uri = r"sqlite:///./db.sqlite"


# Base config class
class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Development config
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = mysql_uri
    SQLALCHEMY_ECHO = True


# Production config
class ProdConfig(Config):
    pass


# Testing config
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = mysql_uri
    SQLALCHEMY_ECHO = False
    Testing=True  # No data gets actually passed into the database