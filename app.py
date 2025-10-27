from flask import Flask
from cilante.auth import auth as auth_blueprint
from cilante.shop import shop as shop_blueprint
from cilante.admin import admin as admin_blueprint
from cilante.assistant import assistant as assistant_blueprint
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(shop_blueprint, url_prefix='/shop')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(assistant_blueprint, url_prefix='/assistant')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)