from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from exts import db
from models.user_models import User, Profile, Message
from models.content_models import Books, Anime, Games
from routes.user import user_ns
from routes.content import content_ns
from routes.forum import forum_ns

def create_app(config):
    """Application factory function"""
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

