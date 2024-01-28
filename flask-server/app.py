from flask import Flask, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from config import DevConfig, TestConfig
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, unset_jwt_cookies, get_jwt_identity, jwt_required
from flask_migrate import Migrate
from exts import db
from models.user_models import User, Profile, Message
from models.content_models import Books, Anime, Games
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
cors = CORS(app, supports_credentials=True)
jwt = JWTManager(app)
# Separated out routes so file doesn't get too big, this file just sets up the app

api = Api(app)  # Passing our app through the Api class from Flask RestX
# api = Api(app, doc="/docs") # So can set the docs to that url


# Model serialiser so can be displayed as a JSON, takes in model class and then the output format
message_model=api.model("Message", {
    "post_id": fields.Integer,
    "post_content": fields.String,
    "post_category": fields.String,
    "post_author": fields.String,
    "post_date": fields.DateTime(dt_format='rfc822')
})

profile_model=api.model("Profile", {
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "date_of_birth": fields.DateTime(dt_format='rfc822'),
    "interests": fields.String
})

user_model=api.model("User", {
    "user_id": fields.String,
    "username": fields.String,
    "password": fields.String
})

books_model=api.model("Books", {
    "Book_ID": fields.Integer,
    "Book_Name": fields.String,
    "Book_Author": fields.String,
    "Book_Genre": fields.String,
    "Price": fields.Float,
    "Book_Script": fields.String,
    "Book_Image": fields.String
})

anime_model=api.model("Anime", {
    "Anime_ID": fields.Integer,
    "Anime_Name": fields.String,
    "Anime_Genre": fields.String,
    "Where_TW": fields.String,
    "Anime_Script": fields.String,
    "Anime_Image": fields.String
})

games_model=api.model("Games", {
    "Game_ID": fields.Integer,
    "Game_Name": fields.String,
    "Game_Genre": fields.String,
    "W_Console": fields.String,
    "Price": fields.Float,
    "Game_Script": fields.String,
    "Game_Image": fields.String
})

# Defining routes

# Creates an access and refresh token which is needed at the front end

def user_access_tokens(user):
    access_token = create_access_token(identity=user.username)
    refresh_token = create_refresh_token(identity=user.username)
    return access_token, refresh_token

# Might use this function to check emails
def check_email(email):
    try:
        v = validate_email(email)
        email = v["email"]
        return True
    except EmailNotValidError as e:
        print(str(e))
        return False
    

@api.route("/hello")
class HomeResource(Resource):
    def get(self):
        return {"message": "hello"}


# Register
# Convert to api model and make a serialiser
@api.route("/register")
class Register(Resource):
    def post(self):
        "Register a new user"
        username = request.json["username"]  # Getting each value from the json
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        email = request.json["email"]
        password = request.json["password"]
        
        username_exists = User.query.filter_by(username=username).first() is not None
        email_exists = Profile.query.filter_by(email=email).first() is not None

        # Ok need to fix something here, it is not liking this return type
        if username_exists:
            return make_response(jsonify({"error": "Username is already taken"}), 409)
        
        if email_exists:
            return make_response(jsonify({"error": "Email is already registered"}), 409)
        
        # Make validation neater later
        if len(username) < 1 or len(username) > 30:
            return make_response(jsonify({"error": "Username must be between 1 and 30 characters"}), 400)
        if len(first_name) < 1 or len(first_name) > 50:
            return make_response(jsonify({"error": "First name must be between 1 and 50 characters"}), 400)
        if len(last_name) < 1 or len(last_name) > 50:
            return make_response(jsonify({"error": "Last name must be between 1 and 50 characters"}), 400)
        if check_email(email) == False:
            return make_response(jsonify({"error": "Email address is invalid"}), 400)

        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        new_profile=Profile(username=username, first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_profile)
        db.session.commit()

        access_token, refresh_token = user_access_tokens(new_user)
        return jsonify(
            {"access_token": access_token, "refresh_token": refresh_token})


# Login
@api.route("/login")
class Login(Resource):
    def post(self):
        "Login a user"
        data=request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        if user is None:
            return make_response(jsonify({"error": "Invalid credentials"}), 401)
        
        if not bcrypt.check_password_hash(user.password, password):
            return make_response(jsonify({"error": "Invalid credentials"}), 401)
        
        access_token, refresh_token = user_access_tokens(user)
        return jsonify(
            {"access_token": access_token, "refresh_token": refresh_token})



# Logout
@app.route("/logout", methods=["POST"])
def logout_user():
    response = jsonify({"message": "Logout successful"})
    # Unset the JWT cookie
    unset_jwt_cookies(response)
    return response

# Message board routes (get and post to any board)
@api.route("/forum")
class ForumResource(Resource):
    # Get all messages, returns a list
    @api.marshal_list_with(message_model)
    def get(self):
        "Get all messages"
        messages = Message.query.all()
        return messages
    
    # Post a message, returns a single message
    @api.marshal_with(message_model)
    @api.expect(message_model)
    def post(self):
        "Create a new message"
        data = request.get_json()
        new_post = Message(
            post_content = data.get("post_content"),
            post_category = data.get("post_category"),
            post_author = data.get("post_author"),
            post_date = data.get("post_date")
        )

        db.session.add(new_post)
        db.session.commit()

        return new_post, 201
    
# Message board route for filtering by category
@api.route("/forum/<string:post_category>")
class ForumCatResource(Resource):
    # Get a post by category

    # Doesn't work think doing it wrong
    @api.marshal_list_with(message_model)
    def get(self, search):
        result = Message.query.filter_by(post_category=search).all()

        return result
    
    #     # Doesn't work think doing it wrong
    # @api.marshal_list_with(message_model)
    # def get(self, post_category):
    #     search = Message.query.filter_by(post_category="{search}").all()

    #     return search


# Content api
# Books    
@api.route("/book_suggestions")
class BooksResource(Resource):
    # Book suggestions

    @api.marshal_list_with(books_model)
    def get(self):
        books = Books.query.all()
        return books
    

# Content api
# Anime    
@api.route("/anime_suggestions")
class AnimeResource(Resource):
    # Anime suggestions

    @api.marshal_list_with(anime_model)
    def get(self):
        anime = Anime.query.all()
        return anime
    
# Content api
# Games
@api.route("/games_suggestions")
class GamesResource(Resource):
    # Game suggestions

    @api.marshal_list_with(games_model)
    def get(self):
        games = Games.query.all()
        return games


# List of all users
@api.route("/users")
class UsersResource(Resource):
    @api.marshal_list_with(profile_model)
    def get(self):
        users=Profile.query.all()
        return users


@api.route("/current_user")
class UserResource(Resource):
    @api.marshal_with(profile_model)
    @jwt_required
    def get(self, current_user):
        current_user = Profile.query.filter_by(username=get_jwt_identity()).first()  # Filter by username (from the JWT token)
        return current_user


# Refresh access token, probably won't have time to implement this on the frontend though
@api.route("/refresh")
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)

        return make_response(jsonify({"access_token": new_access_token}), 200)


if __name__ == "__main__":
    app.run(debug=True)