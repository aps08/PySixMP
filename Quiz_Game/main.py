import requests
from ui_model import *
# Getting data from the an API 
json_data = requests.get("https://opentdb.com/api.php?amount=10").json()["results"]
# This variable stores all the questions as an question model object
question_bank = [Question_Model(question=data["question"], correct=data["correct_answer"],
                                incorrect=data["incorrect_answers"]) for data in json_data]
# Creating objects for classes to run the game.
Q = Quiz_brain(question_bank)
Q_ui = Interface(Q)