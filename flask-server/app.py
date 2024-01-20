from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config import DevConfig, TestConfig
from flask_jwt_extended import JWTManager


# Separated out routes so file doesn't get too big, this file just sets up the app

db = SQLAlchemy()
bcrypt = Bcrypt()
cors = CORS()
jwt = JWTManager()

def create_app(test_config=None):  # Changed function to take in a config so can unit test with a test config
    app = Flask(__name__)
    if test_config is None:
        # Load the instance config when not testing
        app.config.from_object(DevConfig)
    else:
        # Load the test config if passwed in
        app.config.from_object(TestConfig)
    
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app, supports_credentials=True)
    jwt.init_app(app)
    
    
    return app

