from turtle import Turtle, Screen, numinput
import random


PROMPT_TEXT = "Enter number of times you want to run the lines.\nDefault value:50"
FONT = ("Courier", 12, "bold")

class confused_lines(Turtle):
    """
    Doc Strings
    """

    def __init__(self) -> None:
        super().__init__()
        self.angle_list = [0, 90, 180, 270]
        self.screen = Screen()
        self.screen.cv._rootwindow.resizable(False, False)
        self.screen.title("Confused Lines! 😉😉😉😉")
        self.screen.bgcolor("lightgrey")
        self.screen.setup(width=800, height=600)
        self.write_instruction()
        self.input = int(numinput(title="Number", prompt=PROMPT_TEXT, default=50,minval=50, maxval=9999))
        self.run()

    def write_instruction(self) -> None:
        self.hideturtle()
        self.pensize(10)
        self.penup()
        self.goto(x=0, y= 270)
        self.pendown()
        self.pencolor("black")
        self.write("Window will close automatically after it's done", align="center", font=(FONT))
        self.penup()
        self.home()
        self.pendown()

    def run(self) -> None:
        for i in range(self.input):
            self.color(['#%06X' % random.randint(0, 0xFFFFFF) for i in range(1)][0])
            self.right(random.choice(self.angle_list))
            self.forward(25)
        

if __name__ == "__main__":
    print("Running.......")
    App = confused_lines()