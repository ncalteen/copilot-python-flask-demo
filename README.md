# GitHub Copilot Demo Python App

This repository is used to demonstrate GitHub Copilot's capabilities. It is a
simple Python/Flask application that uses the
[GitHub API](https://docs.github.com/en/rest) to retrieve a user's repositories
and display them in a list.

When initially creating the app, I used GitHub Copilot to generate the majority
of the code, with only minor manual tweaks (e.g. removing suggested columns,
changing function names, etc.). There are some challenge steps listed below that
you can try out to see how GitHub Copilot works!

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
> [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).
>
> The token will need `public_repo` scope in order to retrieve public
> repositories.

To run the application locally, you'll need to follow these steps:

1. Clone this repository to your local machine.
1. Navigate to the root directory of the repository.
1. Create a new virtual environment:

   ```bash
   python -m venv venv
   ```

1. Activate the virtual environment:

   Unix-based systems:

   ```bash
   source venv/bin/activate
   ```

   Windows:

   ```cmd
   venv\Scripts\activate
   ```

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. Start the application:

   ```bash
   export FLASK_APP=github_user_app
   export FLASK_ENV=development
   flask run --debug
   ```

1. Open your web browser and go to `http://localhost:5000/` to view the
   application.

   If everything is set up correctly, you should see a landing page.

   To search for a specific user's repositories, navigate to
   `http://localhost:5000/users/<handle>`, e.g.
   `http://localhost:5000/users/ncalteen`.

> **Note:** If you encounter any issues running the application, make sure that
> you have all the necessary dependencies installed, that you're running the
> correct version of Python, and that your virtual environment is activated.
