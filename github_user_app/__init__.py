"""
This module defines the Flask app and routes for the GitHub User App application.
"""
import os
from flask import Flask
from .views import index, user_detail
from .db import db
from .config import Config


def create_app():
    """
    Create and configure an instance of the Flask application.

    Args:
        test_config: A dictionary of configuration values to use when testing.

    Returns:
        The Flask application.
    """
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder="static",
        static_url_path="/static",
    )

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/users/<string:handle>", view_func=user_detail)

    return app
