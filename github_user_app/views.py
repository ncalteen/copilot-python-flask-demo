"""
This module defines the Flask views for the GitHub User App application.
"""

from flask import render_template


def index():
    """
    Render the index page.

    Returns:
        The rendered index.html template.
    """
    return render_template("index.html")


def user_detail(handle):
    """
    Render the user detail page for the given handle.

    Args:
        handle: The handle of the user to display.

    Returns:
        The rendered user_detail.html template with the user's handle.
    """
    # TODO: Get user information from handle
    return render_template("user_detail.html", handle=handle)
