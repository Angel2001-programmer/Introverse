from flask_restx import Resource, Namespace, fields
from exts import db
from models.content_models import Books, Anime, Games

content_ns = Namespace("content", description="A namespace for content recommendations.")

books_model = content_ns.model("Books", {
    "book_id": fields.Integer(description="ID - primary key, autoincrement from 1"),
    "book_name": fields.String(description="Book title, unique"),
    "book_author": fields.String(description="Author of the book"),
    "book_genre": fields.String(description="Genre of the book"),
    "price": fields.Float(description="Recommended retail price"),
    "book_script": fields.String(description="Description of the book"),
    "book_image": fields.String(description="URL of image, unique")
})

anime_model = content_ns.model("Anime", {
    "anime_id": fields.Integer(description="ID - primary key, autoincrement from 1"),
    "anime_name": fields.String(description="Anime title, unique"),
    "anime_genre": fields.String(description="Genre of the anime"),
    "where_tw": fields.String(description="Where to watch the anime"),
    "anime_script": fields.String(description="Description of the anime"),
    "anime_image": fields.String(description="URL of image, unique")
})

games_model = content_ns.model("Games", {
    "game_id": fields.Integer(description="ID - primary key, autoincrement from 1"),
    "game_name": fields.String(description="Game title, unique"),
    "game_genre": fields.String(description="Genre of the game"),
    "w_console": fields.String(description="Which consoles the game is available on"),
    "price": fields.Float(description="Recommended retail price"),
    "game_script": fields.String(description="Description of the game"),
    "game_image": fields.String(description="URL of image, unique")
})


@content_ns.route("/books")
class BooksAll(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self):
        """Get all book suggestions"""
        books = Books.query.all()
        return books


@content_ns.route("/books/id/<int:id>")
class BookById(Resource):

    @content_ns.marshal_with(books_model)
    def get(self, id):
        """Get a book by id"""
        book = Books.query.get_or_404(id)

        return book
    

@content_ns.route("/books/genre/<string:genre>")
class BooksByGenre(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self, genre):
        """Get a book by genre"""
        book = Books.query.filter(Books.book_genre == genre).all()

        return book
    

@content_ns.route("/books/author/<string:author>")
class BooksByAuthor(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self, author):
        """Get a book by author"""
        book = Books.query.filter(Books.book_author.ilike(f"%{author}%")).all()

        return book
    

@content_ns.route("/books/title/<string:title>")
class BooksByName(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self, title):
        """Get a book by title"""
        book = Books.query.filter(Books.book_name.ilike(f"%{title}%")).all()

        return book
    

@content_ns.route("/anime")
class AnimeAll(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self):
        """Get all anime suggestions"""
        anime = Anime.query.all()
        return anime
    

@content_ns.route("/anime/id/<int:id>")
class AnimeById(Resource):

    @content_ns.marshal_with(anime_model)
    def get(self, id):
        """Get an anime by id"""
        anime = Anime.query.get_or_404(id)

        return anime
    
@content_ns.route("/anime/genre/<string:genre>")
class AnimeByGenre(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self, genre):
        """Get an anime by genre"""
        anime = Anime.query.filter(Anime.anime_genre == genre).all()

        return anime
    

@content_ns.route("/anime/stream/<string:stream>")
class AnimeByStream(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self, stream):
        """Get an anime by where to watch"""
        anime = Anime.query.filter(Anime.where_tw.ilike(f"%{stream}%")).all()

        return anime
    
    
@content_ns.route("/anime/title/<string:title>")
class AnimeByName(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self, title):
        """Get an anime by title"""
        anime = Anime.query.filter(Anime.anime_name.ilike(f"%{title}%")).all()

        return anime
    

@content_ns.route("/games")
class GamesAll(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self):
        """Get all game suggestions"""
        games = Games.query.all()
        return games


@content_ns.route("/games/id/<int:id>")
class GameById(Resource):

    @content_ns.marshal_with(games_model)
    def get(self, id):
        """Get a game by id"""
        game = Games.query.get_or_404(id)

        return game
    

@content_ns.route("/games/genre/<string:genre>")
class GamesByGenre(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self, genre):
        """Get a game by genre"""
        game = Games.query.filter(Games.game_genre == genre).all()

        return game

@content_ns.route("/games/console/<string:console>")
class GamesByConsole(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self, console):
        """Get a game by console"""
        game = Games.query.filter(Games.w_console.ilike(f"%{console}%")).all()

        return game
    

@content_ns.route("/games/title/<string:title>")
class GamesByName(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self, title):
        """Get a game by title"""
        game = Games.query.filter(Games.game_name.ilike(f"%{title}%")).all()

        return game


@content_ns.route("/hello")
class Hello(Resource):

    def get(self):
        """Basic route to test"""
        return {"message": "Hello world!"}