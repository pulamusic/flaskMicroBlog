# Flask Micro-Blog

Created from a [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) YouTube video series on [coding with Flask](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).
* **NOTE**: I began this project from a web series from [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA), but I couldn't get the [MySQL](https://www.mysql.com/) database working.

---

### Notes:
* ~~Run `export FLASK_APP=flaskblog.py`, then `export FLASK_DEBUG=1`, then input `flask run` to start the development server.~~
  - ~~Fuck, this is producing an error. I need to debug this before moving on.~~
* ~~**Nope, scratch the last**. I created an `.env` file to take care of part of this, and I reconfigured some of the `flaskblog.py` code as per an issue on [StackOverflow](https://stackoverflow.com/questions/55322179/flask-debug-mode-gives-an-oserror-errno-8-exec-format-error-when-running-us).~~
  - ~~Just run `flask run` to start the development server.~~
  - ~~**Fuck, Fuck, Fuck**, it doesn't work! I'm going to work for a while without the Flask debug option, but I really need to sort this out.~~
  - ~~Nope, now I've got it! Run `python3 flaskblog.py` to start the dev server.~~
  - **IMPORTANT**: I changed the structure of the project. Now I need to run `python3 run.py` in order to start the development server.
* **NOTE**: Consider submitting this project as the [final project for CS50W](https://docs.cs50.net/web/2019/x/projects/final/final.html).
* The local development database is [SQLite](https://www.sqlite.org/index.html). The production version will switch to an online version of [PostgreSQL](https://www.postgresql.org/).
* Check out [WTForms](https://wtforms.readthedocs.io/en/stable/#) for info on [validation](https://wtforms.readthedocs.io/en/stable/validators.html).
  - See `forms.py`.
* Check out the [documentation](https://flask-login.readthedocs.io/en/latest/) for `flask-login`.
* **NOTE**: This app will eventually be deployed to [Heroku](https://www.heroku.com/). Be sure to add it to my portfolio.
* Figure out, at some point, how to create tests for this codebase. Check out the [documentation of Flask testing](https://flask.palletsprojects.com/en/1.1.x/testing/).
  - What other testing frameworks could I use? Check out [this article on Medium](https://medium.com/@neeti.jain/how-to-do-unit-testing-in-flask-and-find-code-coverage-fa5201399bc4).
