from tkinter import *
import random
from quiz_brain import Quiz_brain

THEME_COLOR = "#375362"
FONT_SCORE = "Arial", "12", "italic"
FONT_QAA = "Arial", "18", "italic"
FONT_OPTION = "Arial", "10", "bold"


class Question_Model:
    def __init__(self, question: str, correct: str, incorrect: list) -> None:
        self.question = question
        self.correct = correct
        self.all_opt = incorrect
        self.all_opt.append(self.correct)


class Interface:

    def __init__(self, quiz: Quiz_brain) -> None:
        self.quiz = quiz
        self._points = 0
        self._window = Tk()
        self._window.resizable(False, False)
        self._window.title("Quiz Game")
        self._window.configure(background=THEME_COLOR, padx=20, pady=20)
        self._score = Label(text=f"Score: {self._points}", fg="white", bg=THEME_COLOR, font=FONT_SCORE)
        self._score.grid(row=0, column=1)
        self._canvas = Canvas(width=300, height=250)
        self._question = self._canvas.create_text(150, 125, width=290, text="Some question, for sample question",
                                                  fill=THEME_COLOR, font=FONT_QAA)
        self._canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self._button_A = Button(text="Option A", bg="white", fg=THEME_COLOR, font=FONT_OPTION,
                                command=lambda: self.check(self._button_A.cget('text')))
        self._button_A.grid(row=2, column=0, pady=5, padx=5)
        self._button_B = Button(text="Option B", bg="white", fg=THEME_COLOR, font=FONT_OPTION,
                                command=lambda: self.check(self._button_B.cget('text')))
        self._button_B.grid(row=3, column=0, pady=5, padx=5)
        self._button_C = Button(text="Option C", bg="white", fg=THEME_COLOR, font=FONT_OPTION,
                                command=lambda: self.check(self._button_C.cget('text')))
        self._button_C.grid(row=2, column=1, pady=5, padx=5)
        self._button_D = Button(text="Option D", bg="white", fg=THEME_COLOR, font=FONT_OPTION,
                                command=lambda: self.check(self._button_D.cget('text')))
        self._button_D.grid(row=3, column=1, pady=5, padx=5)
        self.set_question_answers()
        self._window.mainloop()

    def set_question_answers(self) -> None:
        q_and_a = self.quiz.next_question()
        random.shuffle(q_and_a.all_opt)
        self._canvas.itemconfig(self._question, text=q_and_a.question)
        try:
            self._button_A["text"] = q_and_a.all_opt[0]
            self._button_B["text"] = q_and_a.all_opt[1]
            self._button_C["text"] = q_and_a.all_opt[2]
            self._button_D["text"] = q_and_a.all_opt[3]
        except IndexError:
            self.set_question_answers()

    def check(self, user_input) -> None:
        if self.quiz.check_answer(user_input):
            self._canvas.configure(bg="green")
            self._points += 1
            self.quiz.points = self._points
            self._score["text"] = f"Score: {self._points}"
        else:
            self._canvas.configure(bg="red")
        self._window.after(1000, self.set_question_answers())
