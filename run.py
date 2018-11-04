import os
import json

import sys
from pprint import pprint
    
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session
    
app = Flask(__name__)
usernames = []
    
@app.route('/', methods=["GET", "POST"])
def riddle_me_this():
    if request.method == 'POST':
        
      return redirect(url_for('game_questions'))
    return render_template("index.html")



@app.route('/game', methods=["GET", "POST"])
def game_questions():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        return redirect("https://riddle-me-this-crist0fer.c9users.io/questions/0", code=302)
        
        
@app.route('/questions/<int:id>', methods=["GET"]) 
def retrieve_question(id):
    with open('data/company.json') as data_file:    
        data = json.load(data_file)
        q = data[id]
        return render_template("game.html", question = q)
        
@app.route('/questions', methods=["POST"])
def post_answer():
    answer = request.form.get("answer")
    qid = int(request.form.get("qid"))
    next_question = "/questions/"+str(qid+1)
    if "answer" == ("answer"):
        return redirect(next_question)
        
    
    

   
'''    
    def write_to_data(filename, data):
        with open(filename, "a") as file:
            file.writelines(data)
 '''   
'''
    def add_users(username):
        if request.method == 'POST':
            data = []
        write_to_data("data"/"users.txt") as json_data:
        data = json.load(json_data)
        return render_template("game.html", page_title="riddle_me_this", company_data=data)
    '''
'''    
    def get_all_users():
        users = []
        with open("data/users.txt", "r") as user_messages:
            users = user_messages.readlines()
        return users
'''        
'''  
    @app.route('game_questions'/'<question_number>')
    def game(question_number):
        
            
        with open("data.company.json", "r") as json_data:
            data=json.load(json_data)
            data = []
            index = int(question_number)
           
        if request.method == "POST":
            user_answer = request.form[ "user_answer", "<question_number>"]
            right_answer = data[index]['answer']
            if user_answer != right_answer:
                def get_question():
                    game_questions = [+1]
                    with open("data.company.json", "r") as json_data:
                        return render_template('game.html')
    

    
                
'''
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)