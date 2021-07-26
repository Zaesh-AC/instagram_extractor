import logging

from flask import Flask, render_template

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template("homepage.html")