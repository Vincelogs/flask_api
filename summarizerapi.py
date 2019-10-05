# -*- coding: utf-8 -*-
"""summarizerapi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19oPerkacCcXWpWHtXgF4JBRe8FNzn97P
"""

# pylint: disable=invalid-name
""" This script loads in a model """

import pickle as p
import traceback
from flask import Flask, request, jsonify



app = Flask(__name__)



@app.route('/api/summarize', methods=[ 'GET','POST'])
def summarize():
    """ Returns summary of articles """
    if model:
        try:
            if request.method == 'POST':
                article = request.json['article']

                summary = model.summarize(article)

                return jsonify(summary=summary)
            return 'Coming soon'
        except Exception:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('You need a trained model first')
        return 'Model not found'

if __name__ == '__main__':
   
    app.run(debug=True)