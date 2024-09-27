import sys
sys.path.append("..")
from exts import db


class Books(db.Model):
    """
    Class model for the Books table.

    Attributes
    ----------
    book_id : int
        id of the book
    book_name : str
        name of the book
    book_author : str
        author of the book
    book_genre : str
        genre of the book
    price : float
        rrp of the book
    book_script : str (text)
        description of the book
    book_image : str
        image url of the book
    """

    __tablename__ = "books"
    book_id = db.Column(db.Integer, primary_key=True, unique=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    book_author = db.Column(db.String(30), nullable=False)
    book_genre = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Float, nullable=False)
    book_script = db.Column(db.String(1000))
    book_image = db.Column(db.String(100), unique=True)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<Book title {self.book_name}, by author {self.book_author}.>"
    
    def _create(self):
        """Adds a new book object to the database."""
        db.session.add(self)
        db.session.commit()
    
    def _delete(self):
        """Deletes a book object from the database."""
        db.session.delete(self)
        db.session.commit()


class Anime(db.Model):
    """
    Class model for the Anime table.

    Attributes
    ----------
    anime_id : int
        id of the anime
    anime_name : str
        name of the anime
    anime_genre : str
        genre of the anime
    where_tw : str
        where to watch the anime
    anime_script : str (text)
        description of the anime
    anime_image : str
        image url of the anime
    """

    __tablename__ = "anime"
    anime_id = db.Column(db.Integer, primary_key=True, unique=True)
    anime_name = db.Column(db.String(50), unique=True, nullable=False)
    anime_genre = db.Column(db.String(25), nullable=False)
    where_tw = db.Column(db.String(25))
    anime_script = db.Column(db.String(1000))
    anime_image = db.Column(db.String(100), unique=True)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<Anime {self.anime_name}>"
    
    def _create(self):
        """Adds a new anime object to the database."""
        db.session.add(self)
        db.session.commit()
    
    def _delete(self):
        """Deletes an anime object from the database."""
        db.session.delete(self)
        db.session.commit()


class Games(db.Model):
    """
    Class model for the Games table.

    Attributes
    ----------
    game_id : int
        id of the game
    game_name : str
        name of the game
    game_genre : str
        genre of the game
    w_console : str
        which consoles the game is available on
    price : float
        rrp of the game
    game_script : str (text)
        description of the game
    game_image : str
        image url of the game
    """

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, unique=True)
    game_name = db.Column(db.String(50), unique=True, nullable=False)
    game_genre = db.Column(db.String(30), nullable=False)
    w_console = db.Column(db.String(100))
    price = db.Column(db.Float, nullable=False)
    game_script = db.Column(db.String(1000))
    game_image = db.Column(db.String(100), unique=True)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<Game {self.game_name}>"
    
    def _create(self):
        """Adds a new game object to the database."""
        db.session.add(self)
        db.session.commit()
    
    def _delete(self):
        """Deletes a game object from the database."""
        db.session.delete(self)
        db.session.commit()
