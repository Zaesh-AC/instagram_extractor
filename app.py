import logging
import os
import zipfile
from zipfile import ZipFile

from plugins import extract_information
from plugins.settings import OUTPUT_DIR

from flask import (
    Flask,
    render_template,
    request,
    send_file
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def get_image_path(post):
    return post[0].split("/")

def get_image_source(post):
    return get_image_path(post)[:3]

def get_image_filename(post):
    return get_image_path(post)[3:4][0]

def get_file_path(post):
    source = "/".join(get_image_source(post))
    filename = get_image_filename(post)
    return f"data/{source}/{filename.split('.')[0]}"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.files["posts"]:
        file = request.files["posts"]
        posts = extract_information(file)
        username = "username" if request.form.get("username") == "" else request.form.get("username")
        zipfile = f"data/{username}.zip"
        with ZipFile(zipfile, mode="x") as zip:
            for post in posts:
                file_path = get_file_path(post)
                with open(f"{file_path}.txt", 'w+') as caption:
                    caption.write(post[1])
                zip.write(f"{file_path}.jpg")
                zip.write(f"{file_path}.txt")
        return send_file(zipfile)
    return render_template("homepage.html")
