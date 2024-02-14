from flask_restx import fields
import sys
sys.path.append("..")
from routes.content import content_ns
from routes.user import user_ns
from routes.forum import forum_ns
# from ..routes.content import content_ns
# from ..routes.user import user_ns
# from ..routes.forum import forum_ns

books_model = content_ns.model("Books", {
    "book_id": fields.Integer,
    "book_name": fields.String,
    "book_author": fields.String,
    "book_genre": fields.String,
    "price": fields.Float,
    "book_script": fields.String,
    "book_image": fields.String
})

anime_model = content_ns.model("Anime", {
    "anime_id": fields.Integer,
    "anime_name": fields.String,
    "anime_genre": fields.String,
    "where_tw": fields.String,
    "anime_script": fields.String,
    "anime_image": fields.String
})

games_model = content_ns.model("Games", {
    "game_id": fields.Integer,
    "game_name": fields.String,
    "game_genre": fields.String,
    "w_console": fields.String,
    "price": fields.Float,
    "game_script": fields.String,
    "game_image": fields.String
})

profile_model = user_ns.model("Profile", {
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "date_of_birth": fields.DateTime(dt_format='rfc822'),
    "interests": fields.String
})

user_model = user_ns.model("User", {
    "user_id": fields.String,
    "username": fields.String,
    "password": fields.String
})

message_model = forum_ns.model("Message", {
    "post_id": fields.Integer,
    "post_content": fields.String,
    "post_category": fields.String,
    "post_author": fields.String,
    "post_date": fields.DateTime(dt_format='rfc822')
})