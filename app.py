import logging
from zipfile import ZipFile

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

def get_image_path(post):
    return post[0].split("/")

def get_image_source(post):
    return get_image_path(post)[:3]

def get_image_filename(post):
    return get_image_path(post)[3:4][0]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.files["posts"]:
        file = request.files["posts"]
        posts = extract_information(file)
        username = request.form.get('username')
        with ZipFile(f"data/{username}.zip", mode="x") as zip:
            for post in posts:
                source = "/".join(get_image_source(post))
                filename = get_image_filename(post)
                file_path = f"data/{source}/{filename.split('.')[0]}"
                with open(f"{file_path}.txt", 'w+') as caption:
                    caption.write(post[1])
                zip.write(f"{file_path}.jpg")
                zip.write(f"{file_path}.txt")
    return render_template("homepage.html")
