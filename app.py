import logging

from plugins import extract_information
from plugins.settings import OUTPUT_DIR

from flask import (
    Flask,
    render_template,
    request,
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["posts"]
        username = request.form.get("username")
        posts = extract_information(file)
        for post in enumerate(posts):
            if f"{OUTPUT_DIR}/{username}/":
                pass
    return render_template("homepage.html")
