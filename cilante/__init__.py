from flask import Flask
from .auth import auth as auth_blueprint
from .shop import shop as shop_blueprint
from .admin import admin as admin_blueprint
from .assistant import assistant as assistant_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(shop_blueprint, url_prefix='/shop')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(assistant_blueprint, url_prefix='/assistant')

    return app