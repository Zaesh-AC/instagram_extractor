import logging
import os
from zipfile import ZipFile

from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from plugins import extract_information, get_file_path
from plugins.getters import get_context_data
from plugins.settings import UPLOAD_FOLDER


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.files["posts"]:
        file = request.files["posts"]
        username = "username" if request.form.get("username") == "" else request.form.get("username")

        filename = f"{username}.zip"
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"{username}_raw_data"))

        posts = extract_information(file)
        with ZipFile(filename, mode="x") as zip:
            for post in posts:
                file_path = get_file_path(post)
                with open(f"{file_path}.txt", 'w+') as caption:
                    caption.write(post[1])
                zip.write(f"{file_path}.jpg")
                zip.write(f"{file_path}.txt")
        return send_file(filename)
    return render_template("homepage.html", **get_context_data())
