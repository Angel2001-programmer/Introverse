import sys
sys.path.append("..")
from exts import db
from uuid import uuid4
from datetime import datetime as dt


def get_uuid():
    """Returns a unique user ID"""
    return uuid4().hex


class User(db.Model):
    """
    Class model for the user accounts table.

    ...

    Attributes
    ----------
    user_id : str
        unique identity code for the user, generated from get_uuid function
    username : str
        username of the user
    password : str
        password of the user, stored as a bcrypt hash

    Methods
    -------
    __repr__
        Returns a string representation of the constructed object.
    """

    __tablename__ = "user_accounts"
    user_id = db.Column(db.String(36), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<User {self.username}>"


class Profile(db.Model):
    """
    Class model for the user profiles table.

    ...

    Attributes
    ----------
    username : str
        username of the user
    first_name : str
        first name of the user
    last_name : str
        last name of the user
    email : str
        email address of the user
    date_of_birth : date
        date of birth of the user
    interests : str (text)
        interests of the user
    date_joined : datetime
        timestamp of sign up for the user

    Methods
    -------
    __repr__
        Returns a string representation of the constructed object.
    """

    __tablename__ = "user_profiles"
    username = db.Column(db.String(30), primary_key=True, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date)  # This option for future functionality of calculating age and age restricting recommendations -> change this to not null when get working
    interests = db.Column(db.Text)
    date_joined = db.Column(db.DateTime(), default=dt.utcnow)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<User {self.username}>"


class Message(db.Model):
    """
    Class model for the message board table.

    ...

    Attributes
    ----------
    post_id : int
        id of the message
    post_content : str (text)
        text content of the message
    post_category : str
        category of the message
    post_author : str
        author of the message
    post_date : datetime
        time and date that the message was posted

    Methods
    -------
    __repr__
        Returns a string representation of the constructed object.
    create
        Adds a new message to the database.
    delete
        Deletes a message from the database.
    """

    __tablename__ = "message_board"
    post_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    post_content = db.Column(db.Text, nullable=False)
    post_category = db.Column(db.String(50), nullable=False)
    post_author = db.Column(db.String(30), nullable=False)  # Change back to being a FK at some point
    post_date = db.Column(db.DateTime(), default=dt.utcnow, nullable=False)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<Message ID {self.post_id}, by user {self.post_author}, posted at {self.post_date}.>"
    
    def create(self):
        """Adds a new message to the database."""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Deletes a message from the database."""
        db.session.delete(self)
        db.session.commit()
