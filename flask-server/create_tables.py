def deploy():
    """Run create all tables for the default database (development database)"""
    from app import create_app, db
    from models.user_models import User, Profile
    from models.forum_models import Message
    from models.content_models import Books, Anime, Games
    app = create_app()
    app.app_context().push()

    db.create_all()

deploy()