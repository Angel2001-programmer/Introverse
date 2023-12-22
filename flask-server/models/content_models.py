from flask_sqlalchemy import SQLAlchemy
from app import db

# db = SQLAlchemy()


# Class for Books table
class Books(db.Model):
    __tablename__ = "Books"
    Book_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Book_Name = db.Column(db.String(100), unique=True, nullable=False)
    Book_Author = db.Column(db.String(30), nullable=False)
    Book_Genre = db.Column(db.String(25), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Book_Script = db.Column(db.String(1000))


# Class for Anime table
class Anime(db.Model):
    __tablename__ = "Anime"
    Anime_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Anime_Name = db.Column(db.String(50), unique=True, nullable=False)
    Anime_Genre = db.Column(db.String(25), nullable=False)
    Where_TW = db.Column(db.String(25))
    Anime_Script = db.Column(db.String(1000))


# Class for Games table
class Games(db.Model):
    __tablename__ = "Games"
    Game_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Game_Name = db.Column(db.String(50), unique=True, nullable=False)
    Game_Genre = db.Column(db.String(30), nullable=False)
    W_Console = db.Column(db.String(100))
    Price = db.Column(db.Float, nullable=False)
    Game_Script = db.Column(db.String(1000))