import sys
import time
from tkinter import messagebox


class Quiz_brain:
    """ This class holds all the logic for updating next, question and checking the answer.
    """
    def __init__(self, qlist: list) -> None:
        """ __init__() --> This is a constructor which is responsible for showing the first question at the start.

        Args:
            qlist (list): stores a list of object which contains question and answers.
        """
        self.question_number = 0
        self.question_list = qlist
        self.points = 0

    def has_questions(self) -> bool:
        """ has_questions() --> This functions is repsonsible for checking if there are any questions left.

        Returns:
            bool: return True, if the expression is True
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> object:
        """ next_question() --> This function is repsonsible for return the next question object. 

        Returns:
            object: return an object of Question_Model type
        """
        if self.has_questions():
            curr_question = self.question_list[self.question_number]
            self.question_number += 1
            return curr_question
        else:
            messagebox.showinfo(title="GAME OVER", message=f'You have scored: {self.points}\n Closing application.')
            sys.exit(0)

    def check_answer(self, user_answer: str) -> bool:
        """ check_answer() --> This functions is responsible for checking, if the answer clicked is correct or not.

        Args:
            user_answer (str): stores the answer which user has answered.

        Returns:
            bool: return True if user's answer and correct answer is correct otherwise return False. 
        """
        return user_answer.lower() == self.question_list[self.question_number - 1].correct.lower()
