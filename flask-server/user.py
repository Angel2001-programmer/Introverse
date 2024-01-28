from flask_restx import Resource, Namespace
from flask import Flask, request, jsonify
from models.user_models import User, Profile, Message
from email_validator import validate_email, EmailNotValidError

user_ns = Namespace("user", description="A namespace for user authentication and services.")

# Register
@app.route("/register", methods=["POST"])
def register_user():
    username = request.json["username"]  # Getting each value from the json
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    email = request.json["email"]
    password = request.json["password"]
    
    username_exists = User.query.filter_by(username=username).first() is not None  # Checking if username is in DB
    email_exists = Profile.query.filter_by(email=email).first() is not None  # Checking if email is in DB

    if username_exists:
        return jsonify({"error": "Username is already taken"}), 409
    
    if email_exists:
        return jsonify({"error": "Email is already registered"}), 409
    
    # Validate input
    if len(username) < 1 or len(username) > 30:
        return jsonify({"error": "Username is invalid"}), 400
    if len(first_name) < 1 or len(first_name) > 50:
        return jsonify({"error": "Name is invalid"}), 400
    if len(last_name) < 1 or len(last_name) > 50:
        return jsonify({"error": "Name is invalid"}), 400
    # add email validation here

    # Hashing the password
    hashed_password = bcrypt.generate_password_hash(password)
    # Creating an instance of User class to add to user_accounts table, user_id will use default generation
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    # db.session.commit()  # Need to commit the insertion of user to then grab the same user_id it generated
    # Create an instance of the Profile class to add to user_profiles table
    new_profile=Profile(username=username, first_name=first_name, last_name=last_name, email=email)
    db.session.add(new_profile)
    db.session.commit()  # Commit profile

    # Creates an access and refresh token which is needed at the front end
    access_token = create_access_token(identity=new_user.username)
    refresh_token = create_refresh_token(identity=new_user.username)
    return jsonify(
        {"access_token": access_token, "refresh_token": refresh_token})