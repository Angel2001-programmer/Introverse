from dotenv import load_dotenv
import os

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


class Config:
    """Base config class"""
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """Development config"""
    SQLALCHEMY_DATABASE_URI = mysql_uri
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    """Production config"""
    pass


class TestConfig(Config):
    """Testing config"""
    SQLALCHEMY_DATABASE_URI = mysql_uri
    SQLALCHEMY_ECHO = False
    Testing=True  # No data gets actually passed into the database