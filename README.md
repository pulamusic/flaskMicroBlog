# Flask Micro-Blog

Created from a [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) YouTube video series on [coding with Flask](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).
* **NOTE**: I began this project from a web series from [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA), but I couldn't get the MySQL database working.

---
### Notes:
* ~~Run `export FLASK_APP=flaskblog.py`, then `export FLASK_DEBUG=1`, then input `flask run` to start the development server.~~
  - ~~Fuck, this is producing an error. I need to debug this before moving on.~~
* **Nope, scratch the last**. I created an `.env` file to take care of part of this, and I reconfigured some of the `flaskblog.py` code as per an issue on [StackOverflow](https://stackoverflow.com/questions/55322179/flask-debug-mode-gives-an-oserror-errno-8-exec-format-error-when-running-us).
  - Just run `flask run` to start the development server.
