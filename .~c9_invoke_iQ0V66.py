import os
import json

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
data = []

@app.route('/')
def riddle_me_this
    return "<hRiddle me This"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)