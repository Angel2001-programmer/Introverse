from flask_restx import fields
import sys
sys.path.append("..")
from ..routes.content import content_ns
from ..routes.user import user_ns
from ..routes.forum import forum_ns

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

message_model=forum_ns.model("Message", {
    "post_id": fields.Integer,
    "post_content": fields.String,
    "post_category": fields.String,
    "post_author": fields.String,
    "post_date": fields.DateTime(dt_format='rfc822')
})