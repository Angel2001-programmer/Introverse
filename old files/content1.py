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


@content_ns.route("/book_suggestions")
class BooksResource(Resource):

    @content_ns.marshal_list_with(books_model)
    def get(self):
        """Get all book suggestions"""
        books = Books.query.all()
        return books


# @content_ns.route("/book_suggestions/<int:Book_ID>")
# class BookIdResource(Resource):

#     @content_ns.marshal_with(books_model)
#     def get(self, BookID):
#         """Get a book by id"""
#         book = Books.query.get_or_404(BookID)

#         return book

@content_ns.route("/book_suggestions/<int:id>")
class BookIdResource(Resource):

    @content_ns.marshal_with(books_model)
    def get(self, id):
        """Get a book by id"""
        book = Books.query.get_or_404(id)

        return book
    

@content_ns.route("/book_suggestions/<string:genre>")
class BookGenreResource(Resource):

    @content_ns.marshal_with(books_model)
    def get(self, genre):
        """Get a book by genre"""
        book = Books.query.filter(Books.Book_Genre == genre).all()

        return book
    

@content_ns.route("/book_suggestions/<string:genre>")
class BookGenreResource(Resource):

    @content_ns.marshal_with(books_model)
    def get(self, genre):
        """Get a book by author"""
        book = Books.query.filter(Books.Book_Genre == genre).all()

        return book
    
# @content_ns.route("/book_suggestions/<string:Book_Genre>")
# class BookGenreResource(Resource):

#     @content_ns.marshal_with(books_model)
#     def get(self, Book_Genre):
#         """Get a book by genre"""
#         book = Books.query.filter_by(Book_Genre).all()

#         return book


# Content api
# Anime    
@content_ns.route("/anime_suggestions")
class AnimeResource(Resource):
    # Anime suggestions

    @content_ns.marshal_list_with(anime_model)
    def get(self):
        """Get all anime suggestions"""
        anime = Anime.query.all()
        return anime
    
# Content api
# Games
@content_ns.route("/games_suggestions")
class GamesResource(Resource):
    # Game suggestions

    @content_ns.marshal_list_with(games_model)
    def get(self):
        """Get all game suggestions"""
        games = Games.query.all()
        return games



"""
Need to test
- If return type ok
"""