from flask import Flask
from .config import Config
from .extensions import db, ma, migrate, jwt
from .routes.auth_routes import auth_bp
from .routes.post_routes import post_bp
from .errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(post_bp, url_prefix="/api/posts")

    register_error_handlers(app)

    return app
