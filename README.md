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
* Using the [itsdangerous](https://pythonhosted.org/itsdangerous/) plugin for data security.
* Using [flask-mail](https://pythonhosted.org/Flask-Mail/) for password reset email.
  - Check [here](https://stackoverflow.com/questions/37058567/configure-flask-mail-to-use-gmail) for directions on how to set up flask-mail with gmail.
  - Yay, I figured out the glitch I had been having with sending the reset email. The firewall at the community college library where I work on coding wasn't allowing me to contact an email server. I've had this problem before with connecting to databases. Fortunately, I can connect to the internet using my phone as a mobile hotspot. Problem solved.
* Restructured the code to be a modular app using [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/).

**NOTE**: At this point, after having finished the first 12 videos, I have finished coding the app. The [13th video](https://youtu.be/goToXTC96Co) is all about deploying the app to the internet using a custom-built Linux server. I'm going to leave it for now, hopefully figuring out how to deploy to Heroku at some point.

---

### What's next for this project

Either get the sidebar to work, or delete it.
