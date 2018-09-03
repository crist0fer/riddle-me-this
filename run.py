import os
import json

from datetime import datetime
from flask import Flask, render_template, redirect

app = Flask(__name__)
usernames = []

def write_to_data(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)

def add_usernames(username):
    write_to_data("data/users.txt", "({0}) - {1}\n".format(
            username.title()))

def get_all_users():
    users = []
    with open("data/users.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users
    

@app.route('/')
def riddle_me_this():
    return render_template("index.html")
    
@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

    riddle_index = 0
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)