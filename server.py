from flask import Flask, request, render_template, redirect, flash, session
from jinja2 import StrictUndefined

import os

app = Flask(__name__)


app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABC123")
# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def home():
	"""Home page"""

	return render_template("index.html")


@app.route("/error")
def error():
	raise Exception("Error!")


@app.route("/resume")
def render_resume_page():
	"""Software Engineer Resume"""

	return render_template("resume.html")

if __name__ == "__main__":

	PORT = int(os.environ.get("PORT", 5000))
	
	#DEBUG = "NO_DEBUG" not in os.environ
	#app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
	app.run(host="0.0.0.0", port=PORT)
