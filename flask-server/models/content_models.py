import sys
sys.path.append("..")
from exts import db


class Books(db.Model):
    """
    Class model for the Books table.

    ...

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

    Methods
    -------
    __repr__
        Returns a string representation of the constructed object.
    create
        Adds a new book object to the database.
    delete
        Deletes a book object from the database.
    """

    __tablename__ = "Books"
    Book_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Book_Name = db.Column(db.String(100), unique=True, nullable=False)
    Book_Author = db.Column(db.String(30), nullable=False)
    Book_Genre = db.Column(db.String(25), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Book_Script = db.Column(db.String(1000))
    Book_Image = db.Column(db.String(100), unique=True)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<Book title {self.Book_Name}, by author {self.Book_Author}.>"
    
    def create(self):
        """Adds a new book object to the database."""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Deletes a book object from the database."""
        db.session.delete(self)
        db.session.commit()


class Anime(db.Model):
    """
    Class model for the Anime table.

    ...

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

    Methods
    -------
    __repr__
        Returns a string representation of the constructed object.
    create
        Adds a new anime object to the database.
    delete
        Deletes a anime object from the database.
    """

    __tablename__ = "Anime"
    Anime_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Anime_Name = db.Column(db.String(50), unique=True, nullable=False)
    Anime_Genre = db.Column(db.String(25), nullable=False)
    Where_TW = db.Column(db.String(25))
    Anime_Script = db.Column(db.String(1000))
    Anime_Image = db.Column(db.String(100), unique=True)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<Anime {self.Anime_Name}>"
    
    def create(self):
        """Adds a new anime object to the database."""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Deletes an anime object from the database."""
        db.session.delete(self)
        db.session.commit()


class Games(db.Model):
    """
    Class model for the Games table.

    ...

    Attributes
    ----------
    game_id : int
        id of the game
    game_name : str
        name of the game
    game_genre : str
        genre of the game
    w_console : str
        which consoles to play the game
    price : float
        rrp of the game
    game_script : str (text)
        description of the game
    game_image : str
        image url of the game

    Methods
    -------
    __repr__
        Returns a string representation of the constructed object.
    create
        Adds a new game object to the database.
    delete
        Deletes a game object from the database.
    """

    __tablename__ = "Games"
    Game_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Game_Name = db.Column(db.String(50), unique=True, nullable=False)
    Game_Genre = db.Column(db.String(30), nullable=False)
    W_Console = db.Column(db.String(100))
    Price = db.Column(db.Float, nullable=False)
    Game_Script = db.Column(db.String(1000))
    Game_Image = db.Column(db.String(100), unique=True)

    def __repr__(self):
        """Returns a string representation of constructed object."""
        return f"<Game {self.Game_Name}>"
    
    def create(self):
        """Adds a new game object to the database."""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Deletes a game object from the database."""
        db.session.delete(self)
        db.session.commit()
