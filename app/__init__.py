from flask import Flask
from app import tasks
from app.extentions import ma, db, migrate


def create_app(config_object='app.config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def register_blueprints(app):
    app.register_blueprint(tasks.routes.bp)
