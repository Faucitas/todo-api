from flask import Flask
from app.extentions import ma, db, migrate


def create_app(config_object='app.config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    # print(app.config.get('SQLALCHEMY_DATABASE_URI'))
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def register_blueprints(app):
    pass
