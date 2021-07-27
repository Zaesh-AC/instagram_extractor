import json
import logging

from flask import Flask, render_template, request
from instagram_extractor import Extractor

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        extractor = Extractor
        for file in request.files["file"]:
            df = extractor.get_dataframe(file)
    return render_template("homepage.html")
