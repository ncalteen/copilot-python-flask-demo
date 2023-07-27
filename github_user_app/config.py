"""
Flask configuration file
"""
import os


class Config:
    """
    Configuration variables
    """

    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "sqlite:///github_user_app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
