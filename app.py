"""
This is a simple Flask application that greets the user with a "Hello, World!" message.

Routes:
- /: Displays the "Hello, World!" message.

Usage:
- Run `python app.py` to start the application.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """
    Displays a "Hello, World!" message to the user.

    Returns:
    A string containing the "Hello, World!" message.
    """
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
