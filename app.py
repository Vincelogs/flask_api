#!/usr/bin/env python3

import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return 'This is home page'

@app.route("/upload", methods=['POST'])
def handleFileUpload():

    msg = 'failed to upload image'

    if 'image' in request.files:

        photo = request.files['image']

        if photo.filename != '':

            photo.save(os.path.join('.', photo.filename))
            msg = 'image uploaded successfully'

    return msg

if __name__ == '__main__':
    app.run()
