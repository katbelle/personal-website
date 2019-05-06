import os
from datadog import api, initialize
from ddtrace import patch_all, config
patch_all()
# Enable distributed tracing
config.flask['distributed_tracing_enabled'] = True

from flask import Flask, request, render_template, redirect, flash, session
from jinja2 import StrictUndefined

# Add and initialize Datadog monitoring.
initialize( 
	api_key='8e2afe5aba8c5cba788e3e46722feaca',
	app_id='f7f37c7d8a664d75500dcff131f89bcd9f602ddc'
)


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
	PORT = int(os.environ.get("PORT", 8080))
	
	# Send a startup event to Datadog.
	title = 'Server-bootup'
	text = '[personal-website]: server booting up'
	tags = ['application:web']

	api.Event.create(title=title, text=text, tags=tags)
	
	#DEBUG = "NO_DEBUG" not in os.environ
	#app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
	app.run(host="0.0.0.0", port=PORT)


