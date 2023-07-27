# GitHub Copilot Demo Python App

This repository is used to demonstrate GitHub Copilot's capabilities. It is a
simple Python/Flask application that uses the
[GitHub API](https://docs.github.com/en/rest) to retrieve a user's repositories
and display them in a list.

## Running the Application Locally

To run the application locally, you'll need to follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the root directory of the repository.
3. Create a new virtual environment by running `python -m venv venv` in your
   terminal.
4. Activate the virtual environment by running `source venv/bin/activate` (on
   Unix-based systems) or `venv\Scripts\activate` (on Windows) in your terminal.
5. Install the required dependencies by running
   `pip install -r requirements.txt` in your terminal.
6. Run the following commands in your terminal:

   ```bash
   export FLASK_APP=github_user_app
   export FLASK_ENV=development
   flask run --debug
   ```

7. Open your web browser and go to `http://localhost:5000/` to view the
   application.

If everything is set up correctly, you should see a "Hello, World!" message
displayed in your browser.

Note: If you encounter any issues running the application, make sure that you
have all the necessary dependencies installed, that you're running the correct
version of Python, and that your virtual environment is activated.
