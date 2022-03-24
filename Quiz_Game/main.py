import requests
from ui_model import *
json_data = requests.get("https://opentdb.com/api.php?amount=10").json()["results"]
question_bank = [Question_Model(question=data["question"], correct=data["correct_answer"],
                                incorrect=data["incorrect_answers"]) for data in json_data]
Q = Quiz_brain(question_bank)
Q_ui = Interface(Q)