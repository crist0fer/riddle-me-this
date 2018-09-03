import os
import json

from datetime import datetime
from flask import Flask, render_template, redirect

app = Flask(__name__)
usernames = []

def add_usernames(username):
    usernames.append("{}".format(username))
    

@app.route('/')
def riddle_me_this():
    return render_template("index.html")
    
@app.route('/<username>')
def user(username):
    add_usernames(username)
    return redirect(username)
    return "Welcome, {0}" + username
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)