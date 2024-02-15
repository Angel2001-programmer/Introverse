import sys
sys.path.append("..")
from exts import db
from datetime import datetime as dt, UTC


class Message(db.Model):
    """
    Class model for the Message Board table.

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
    """

    __tablename__ = "message_board"
    post_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    post_content = db.Column(db.Text, nullable=False)
    post_category = db.Column(db.String(50), nullable=False)
    post_author = db.Column(db.String(30), nullable=False)  # Change back to being a FK at some point
    post_date = db.Column(db.DateTime(), default=dt.now(UTC), nullable=False)

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

    def update(self, post_content):
        """Updates a message in the database."""
        self.post_content = post_content

        db.session.commit()