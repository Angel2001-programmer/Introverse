from flask_restx import Resource, Namespace, fields
from flask import request, jsonify, make_response
from models.user_models import User, Profile
from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies, get_jwt_identity, jwt_required
from email_validator import validate_email, EmailNotValidError
from exts import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

user_ns = Namespace("user", description="A namespace for user authentication and services.")

profile_model=user_ns.model("Profile", {
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "date_of_birth": fields.DateTime(dt_format='rfc822'),
    "interests": fields.String
})

user_model=user_ns.model("User", {
    "user_id": fields.String,
    "username": fields.String,
    "password": fields.String
})


def user_access_tokens(user):
    """Return an access and refresh token for the user"""
    access_token = create_access_token(identity=user.username)
    refresh_token = create_refresh_token(identity=user.username)
    return access_token, refresh_token

def check_email(email):
    """Validate email function, return True if valid format"""
    try:
        v = validate_email(email)
        email = v["email"]
        return True
    except EmailNotValidError as e:
        print(str(e))
        return False


@user_ns.route("/register")
class Register(Resource):
    def post(self):
        """Register a new user"""
        username = request.json["username"]
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        email = request.json["email"]
        password = request.json["password"]
        
        username_exists = User.query.filter_by(username=username).first() is not None
        email_exists = Profile.query.filter_by(email=email).first() is not None

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
        return make_response(jsonify(
            {"access_token": access_token, "refresh_token": refresh_token, "user": new_user.username}), 201)   


@user_ns.route("/login")
class Login(Resource):
    def post(self):
        """Login a user"""
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        if user is None:
            return make_response(jsonify({"error": "Invalid credentials"}), 401)
        
        if not bcrypt.check_password_hash(user.password, password):
            return make_response(jsonify({"error": "Invalid credentials"}), 401)
        
        access_token, refresh_token = user_access_tokens(user)
        return make_response(jsonify(
            {"access_token": access_token, "refresh_token": refresh_token, "user": user.username}), 200)


@user_ns.route("/logout")
class Logout(Resource):
    def post(self):
        """Logout a user"""
        response = jsonify({"message": "Logout successful"})
        unset_jwt_cookies(response)
        return response
    

@user_ns.route("/refresh")
class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """Refresh access token"""
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)

        return make_response(jsonify({"access_token": new_access_token}), 200)
    

@user_ns.route("/current_user")
class CurrentUser(Resource):
    @user_ns.marshal_with(profile_model)
    @jwt_required()
    def get(self, current_user):
        """Get current user by username, need to investigate issue with get identity, returns null"""
        current_user = Profile.query.filter_by(username=get_jwt_identity()).first()  # Filter by username (from the JWT token)
        return current_user


@user_ns.route("/members")
class UsersResource(Resource):
    @user_ns.marshal_list_with(profile_model)
    def get(self):
        """List all users"""
        users=Profile.query.all()
        return users
    

@user_ns.route("/members/<string:member>")
class MemberResource(Resource):
    @user_ns.marshal_with(profile_model)
    def get(self, member):
        """List a member"""
        user = Profile.query.filter(Profile.username == member).first()
        return user

