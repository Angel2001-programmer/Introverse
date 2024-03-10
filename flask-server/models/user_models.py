import sys
sys.path.append("..")
from exts import db
from uuid import uuid4
from datetime import datetime as dt, UTC


def get_uuid():
    """Returns a unique user ID"""
    return uuid4().hex


class User(db.Model):
    """
    Class model for the User Accounts table.

    Attributes
    ----------
    user_id : str
        unique identity code for the user, generated from get_uuid function
    username : str
        username of the user
    password : str
        password of the user, stored as a bcrypt hash
    """

    __tablename__ = "user_accounts"
    user_id = db.Column(db.String(36), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<User {self.username}:ID {self.user_id}>"
    

class Profile(db.Model):
    """
    Class model for the User Profiles table.

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
    """

    __tablename__ = "user_profiles"
    username = db.Column(db.String(30), primary_key=True, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date)  # This option for future functionality of calculating age and age restricting recommendations -> change this to not null when get working
    interests = db.Column(db.Text)
    date_joined = db.Column(db.DateTime(), default=dt.now(UTC))

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<User {self.username}: {self.first_name} {self.last_name}: {self.email} >"

    def update_interests(self, interests):
        """Updates profile in the database."""
        self.interests = interests
        db.session.commit()

    def update_dob(self, dob):
        """Updates profile in the database."""
        self.date_of_birth = dob
        db.session.commit()

