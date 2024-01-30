from flask_restx import Resource, Namespace, fields
from flask import Flask, request, jsonify, make_response
from exts import db
from models.content_models import Books, Anime, Games


content_ns = Namespace("content", description="A namespace for content recommendations.")

books_model=content_ns.model("Books", {
    "Book_ID": fields.Integer,
    "Book_Name": fields.String,
    "Book_Author": fields.String,
    "Book_Genre": fields.String,
    "Price": fields.Float,
    "Book_Script": fields.String,
    "Book_Image": fields.String
})

anime_model=content_ns.model("Anime", {
    "Anime_ID": fields.Integer,
    "Anime_Name": fields.String,
    "Anime_Genre": fields.String,
    "Where_TW": fields.String,
    "Anime_Script": fields.String,
    "Anime_Image": fields.String
})

games_model=content_ns.model("Games", {
    "Game_ID": fields.Integer,
    "Game_Name": fields.String,
    "Game_Genre": fields.String,
    "W_Console": fields.String,
    "Price": fields.Float,
    "Game_Script": fields.String,
    "Game_Image": fields.String
})


@content_ns.route("/books")
class BooksResource(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self):
        """Get all book suggestions"""
        books = Books.query.all()
        return books


@content_ns.route("/books/id/<int:id>")
class BookIdResource(Resource):

    @content_ns.marshal_with(books_model)
    def get(self, id):
        """Get a book by id"""
        book = Books.query.get_or_404(id)

        return book
    

@content_ns.route("/books/genre/<string:genre>")
class BookGenreResource(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self, genre):
        """Get a book by genre"""
        book = Books.query.filter(Books.Book_Genre == genre).all()

        return book
    

@content_ns.route("/books/author/<string:author>")
class BookAuthorResource(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self, author):
        """Get a book by author"""
        book = Books.query.filter(Books.Book_Author.ilike(f"%{author}%")).all()

        return book
    

@content_ns.route("/books/title/<string:title>")
class BookNameResource(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self, title):
        """Get a book by title"""
        book = Books.query.filter(Books.Book_Name.ilike(f"%{title}%")).all()

        return book
    

@content_ns.route("/anime")
class AnimeResource(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self):
        """Get all anime suggestions"""
        anime = Anime.query.all()
        return anime
    

@content_ns.route("/anime/id/<int:id>")
class AnimeIdResource(Resource):

    @content_ns.marshal_with(anime_model)
    def get(self, id):
        """Get an anime by id"""
        anime = Anime.query.get_or_404(id)

        return anime
    
@content_ns.route("/anime/genre/<string:genre>")
class AnimeGenreResource(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self, genre):
        """Get an anime by genre"""
        anime = Anime.query.filter(Anime.Anime_Genre == genre).all()

        return anime
    

@content_ns.route("/anime/stream/<string:stream>")
class AnimeStreamResource(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self, stream):
        """Get an anime by where to watch"""
        anime = Anime.query.filter(Anime.Where_TW.ilike(f"%{stream}%")).all()

        return anime
    
    
@content_ns.route("/anime/title/<string:title>")
class AnimeNameResource(Resource):

    @content_ns.marshal_list_with(anime_model)
    def get(self, title):
        """Get an anime by title"""
        anime = Anime.query.filter(Anime.Anime_Name.ilike(f"%{title}%")).all()

        return anime
    

@content_ns.route("/games")
class GamesResource(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self):
        """Get all game suggestions"""
        games = Games.query.all()
        return games


@content_ns.route("/games/id/<int:id>")
class GameIdResource(Resource):

    @content_ns.marshal_with(games_model)
    def get(self, id):
        """Get a game by id"""
        game = Games.query.get_or_404(id)

        return game
    

@content_ns.route("/games/genre/<string:genre>")
class GameGenreResource(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self, genre):
        """Get a game by genre"""
        game = Games.query.filter(Games.Game_Genre == genre).all()

        return game

@content_ns.route("/games/console/<string:console>")
class GameConsoleResource(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self, console):
        """Get a game by console"""
        game = Games.query.filter(Games.W_Console.ilike(f"%{console}%")).all()

        return game
    

@content_ns.route("/games/title/<string:title>")
class GameNameResource(Resource):

    @content_ns.marshal_list_with(games_model)
    def get(self, title):
        """Get a game by title"""
        game = Games.query.filter(Games.Game_Name.ilike(f"%{title}%")).all()

        return game

"""
Need to test
- If return type ok
"""