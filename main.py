from flask import Flask, request, abort, send_file
import img_processing
import random
import os
from pdf2image import convert_from_path
from dotenv import load_dotenv

app = Flask(__name__)


@app.route("/")
def index():
    return "Nothing here :("


@app.route("/combine", methods=["POST"])
def combine_images():
    API_KEY = os.getenv("API_KEY")
    if API_KEY is None:
        API_KEY = ""

    if request.args.get("API_KEY", default="") != API_KEY:
        abort(401, "Invalid API_KEY")

    if "images" not in request.files:
        abort(400, "No images provided")

    images = request.files.getlist("images")

    if len(images) == 0:
        abort(400, "No images provided")

    image_data = img_processing.images_to_data(images)
    return_data, tmp_file = img_processing.images_to_return_data(image_data)

    return send_file(return_data, download_name=tmp_file, mimetype="image/jpeg")


@app.route("/pdf2img", methods=["POST"])
def pdf_to_image():
    API_KEY = os.getenv("API_KEY")

    if API_KEY is None:
        API_KEY = ""

    if request.args.get("API_KEY", default="") != API_KEY:
        abort(401, "Invalid API_KEY")

    if "pdf" not in request.files:
        abort(400, "No pdf provided")

    pdf = request.files["pdf"]
    tmp_file = str(random.randint(100000, 9999999)) + ".pdf"
    pdf.save(tmp_file)
    images = convert_from_path(tmp_file)
    os.remove(tmp_file)

    image_data = img_processing.images_to_data(images)
    return_data, tmp_file = img_processing.images_to_return_data(image_data)

    return send_file(return_data, download_name=tmp_file, mimetype="image/jpeg")


if __name__ == "__main__":
    load_dotenv()
    app.run()
