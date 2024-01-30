from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restx import Api, Resource
from config import DevConfig, TestConfig
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from exts import db
from models.user_models import User, Profile, Message
from models.content_models import Books, Anime, Games
# from email_validator import validate_email, EmailNotValidError
from user import user_ns
from content import content_ns
from forum import forum_ns
# Finish off moving to ns and delete what don't need

# Application factory function
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)
    cors = CORS(app, supports_credentials=True)
    jwt = JWTManager(app)

    api = Api(app)

    api.add_namespace(user_ns)
    api.add_namespace(content_ns)
    api.add_namespace(forum_ns)

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

