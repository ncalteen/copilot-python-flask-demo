# GitHub Copilot Demo Python App

This repository is used to demonstrate GitHub Copilot's capabilities. It is a
simple Python/Flask application that uses the
[GitHub API](https://docs.github.com/en/rest) to retrieve a user's repositories
and display them in a list.

## Challenges

Using **only** GitHub Copilot, try to complete the following challenges:

- [ ] Add a "Search" form to the application that allows the user to search for
      a GitHub user by username.
- [ ] Add a link to each public repository that allows the user to view the
      repository on GitHub.
- [ ] Get the actual contribution number for each repository (**hint:** You'll
      need to use either the
      [List repository contributors](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-contributors)
      REST API, or the
      [user](https://docs.github.com/en/graphql/reference/queries#user) GraphQL
      API).

## Running the Application Locally

> **Note:** You will need to set the GITHUB_TOKEN environment variable to a
> valid personal access token PAT in order to run the application locally. For
> instructions, see
> [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)

To run the application locally, you'll need to follow these steps:

1. Clone this repository to your local machine.
1. Navigate to the root directory of the repository.
1. Create a new virtual environment by running `python -m venv venv` in your
   terminal.
1. Activate the virtual environment by running `source venv/bin/activate` (on
   Unix-based systems) or `venv\Scripts\activate` (on Windows) in your terminal.
1. Install the required dependencies by running
   `pip install -r requirements.txt` in your terminal.
1. Run the following commands in your terminal:

   ```bash
   export FLASK_APP=github_user_app
   export FLASK_ENV=development
   flask run --debug
   ```

1. Open your web browser and go to `http://localhost:5000/` to view the
   application.

If everything is set up correctly, you should see a "Hello, World!" message
displayed in your browser.

Note: If you encounter any issues running the application, make sure that you
have all the necessary dependencies installed, that you're running the correct
version of Python, and that your virtual environment is activated.
