"""
This module defines the Flask app and routes for the GitHub User App application.
"""
import os
from flask import Flask
from github_user_app.views import index, user_detail


def create_app(test_config=None):
    """
    Create and configure an instance of the Flask application.

    Args:
        test_config: A dictionary of configuration values to use when testing.

    Returns:
        The Flask application.
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # Not testing
        # Load the instance config
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Testing
        # Load the test config
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/user/<string:handle>", view_func=user_detail)

    return app
