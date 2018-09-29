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
      return redirect(url_for('game_questions'))
    return render_template("index.html")


@app.route('/game', methods=["GET", "POST"])
def game_questions():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        return render_template("game.html", page_title="riddle_me_this", company_data=data)
      

   
    
    def write_to_data(filename, data):
        with open(filename, "a") as file:
            file.writelines(data)
    
    
    def add_users(username):
        write_to_data("data/users.txt", "r")
    
    
    def get_all_users():
        users = []
        with open("data/users.txt", "r") as user_messages:
            users = user_messages.readlines()
        return users
        
        
    @app.route('/<question_number>')
    def game(question_number):
        username = session.get('username')
        if request.method == 'POST':
            data = []
            with open("data.company.json", "r") as json_data:
                data=json.load(json_data)
                
            # here comes the answer processing
            pass
        
        # get question from the file using question_number
        def get_question():
            questions = []
            with open("data.company.json", "r") as json_data:
                return render_template('game.html')
    

    
                
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)