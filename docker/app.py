import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from src.api import list_files, download_file, upload_file
from PIL import Image
from io import BytesIO  
import albumentations as albu

app = Flask(__name__)
BUCKET = "my-app-bucket-kirill"


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/storage")
def storage():
    contents = list_files("flaskdrive")
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        h, w = int(request.form['height']), int(request.form['width'])
        image = Image.open(f)
        image = image.resize((w, h))
        image_stream = BytesIO()
        image.save(image_stream, format='JPEG')
        image_stream.seek(0)
        f.stream = image_stream
        f.filename = f"{w}_{h}_{f.filename}"
        print(f.filename)
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)
        return redirect("/storage")


if __name__ == '__main__':
    app.run(debug=True)