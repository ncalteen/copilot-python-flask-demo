"""
This module defines the data models for the GitHub User App application.
"""

from .db import db


class User(db.Model):
    """
    Represents a user in the application.
    """

    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(80), unique=True, nullable=False)
    repositories = db.relationship("Repository", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.handle}>"


class Repository(db.Model):
    """
    Represents a repository for a user.
    """

    id = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String(80), nullable=False)
    contributions = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"<Repository {self.repo_name}>"
