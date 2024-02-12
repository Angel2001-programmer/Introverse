from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restx import Api
from flask_migrate import Migrate
from exts import db, jwt
from config import DevConfig, TestConfig
from models.user_models import User, Profile, Message
from models.content_models import Books, Anime, Games
from routes.user import user_ns
from routes.content import content_ns
from routes.forum import forum_ns

bcrypt = Bcrypt()
cors = CORS()
migrate = Migrate()

def create_app(test_config=None):
    """Application factory function"""
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(TestConfig)
    
    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    cors.init_app(app, supports_credentials=True)
    jwt.init_app(app)

    api = Api(app)

    api.add_namespace(user_ns)
    api.add_namespace(content_ns)
    api.add_namespace(forum_ns)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "token_expired"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message": "Signature verification failed", "error": "invalid_token"}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({"message": "Request does not contain a valid token", "error": "authorisation_token"}), 401

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "User": User,
            "Profile": Profile,
            "Message": Message,
            "Books": Books,
            "Anime": Anime,
            "Games": Games
        }

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)