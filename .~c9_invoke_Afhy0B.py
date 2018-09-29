import os
import json

from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
usernames = []

@app.route('/', methods=["GET", "POST"])
def riddle_me_this():
    if request.method == 'POST':
        # store the username from the form in the session
        return redirect(url_for('game', question_number=0))
    return render_template("index.html")

def write_to_data(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)


def add_users(username):
    write_to_data("data/users.txt")


def get_all_users():
    users = []
    with open("data/users.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users
    
    
@app.route('/game/<question_number>')
def game(question_number):
    username = session['username']
    if request.method == 'POST':
        # here comes the answer processing
        pass
    
    # get question from the file using question_number
    question = get_question(question_number)
    return render_template(
        userna
        
        question_name='riddle_0',
        question_desc='The more you take, the more you leave behind, what am i?') 
   

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

            


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)