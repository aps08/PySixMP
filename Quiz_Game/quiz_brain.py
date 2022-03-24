import sys
import time
# from ui_model import Question_Model
from tkinter import messagebox


class Quiz_brain:
    def __init__(self, qlist: list) -> None:
        self.question_number = 0
        self.question_list = qlist
        self.points = 0

    def has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.has_questions():
            curr_question = self.question_list[self.question_number]
            self.question_number += 1
            return curr_question
        else:
            messagebox.showinfo(title="GAME OVER", message=f'You have scored: {self.points}\n Closing application.')
            sys.exit(0)

    def check_answer(self, user_answer: str) -> bool:
        return user_answer.lower() == self.question_list[self.question_number - 1].correct.lower()
