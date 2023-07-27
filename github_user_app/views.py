"""
This module defines the Flask views for the GitHub User App application.
"""

import os
import requests
from flask import render_template
from .models import User, Repository
from .db import db


def index():
    """
    Render the index page.

    Returns:
        The rendered index.html template.
    """
    users = User.query.all()
    return render_template("index.html", users=users)


def user_detail(handle):
    """
    Render the user detail page for the given handle.

    Args:
        handle: The handle of the user to display.

    Returns:
        The rendered user_detail.html template with the user's handle and repository list.
    """
    # Get user information from handle
    headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
    user_url = f"https://api.github.com/users/{handle}"
    user_response = requests.get(user_url, headers=headers, timeout=5)
    user_data = user_response.json()

    # Create or update user record in database
    user = User.query.filter_by(handle=handle).first()
    if user is None:
        user = User(handle=handle)
        db.session.add(user)
    db.session.commit()

    # Get repository information for user
    repos_url = user_data["repos_url"]
    repos_response = requests.get(repos_url, headers=headers, timeout=5)
    repos_data = repos_response.json()

    # Create or update repository records in database
    for repo in repos_data:
        repository = Repository.query.filter_by(repo_name=repo["name"]).first()
        if repository is None:
            repository = Repository(repo_name=repo["name"], user_id=user.id)
            db.session.add(repository)
        else:
            repository.user_id = user.id
    db.session.commit()

    # Get list of repositories for user
    repos = Repository.query.filter_by(user_id=user.id).all()

    # Extract repository names and contributions
    # TODO: Get contributions for a user and a specific repository
    repositories = []
    for repo in repos_data:
        repo_name = repo["name"]
        contributions = 0
        repositories.append({"repo_name": repo_name, "contributions": contributions})

    return render_template("user_detail.html", handle=handle, repos=repos)
