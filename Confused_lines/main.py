from tkinter import TclError
from turtle import Terminator, Turtle, Screen, numinput
import random, time

PROMPT_TEXT = "Enter number of times you want to run the lines.\nDefault value:50"
FONT = ("Courier", 12, "bold")
X = 400.0
Y = 300.0
ANGLES = [0, 90, 180, 270]
FORWARD_BY = [30, 50, 70]

class confused_lines(Turtle):
    """
    Summary of the class:
    This class is responsible for runnig the confused lines and inherits the turtle object.

    Funcions and uses:
    1. __init__() --> Constructor. Creates the screen and takes the input from user.
    2. write_instructions() --> responsible for showing text on the screen.
    3. run() --> run the loop N times, which is taken from the user, by default the value is 50.
    4. mirror() --> responsible for mirroring the turtle.
    """

    def __init__(self) -> None:
        super().__init__()
        self.screen = Screen()
        self.screen.cv._rootwindow.resizable(False, False)
        self.screen.title("Confused Lines! 😉😉😉😉")
        self.screen.bgcolor("black")
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
        self.pencolor("white")
        self.write("Window will close automatically after it's done", align="center", font=(FONT))
        self.penup()
        self.home()
        self.pendown()

    def run(self) -> None:
        for i in range(self.input):
            self.mirror()
            self.color(['#%06X' % random.randint(0, 0xFFFFFF) for i in range(1)][0])
            self.right(random.choice(ANGLES))
            self.forward(random.choice(FORWARD_BY))
        self.clear()
        self.penup()
        self.home()
        self.pendown()
        self.pencolor("white")
        self.write("Closing window in 3 seconds", align="center", font=FONT)
        time.sleep(3)

    def mirror(self) -> None:
        if self.xcor() < -X:
            self.penup()
            self.goto(X, self.ycor())
            self.pendown()
        if self.xcor() > X:
            self.penup()
            self.goto(-X, self.ycor())
            self.pendown()
        if self.ycor() < -Y:
            self.penup()
            self.goto(self.xcor(), Y)
            self.pendown()
        if self.ycor() > Y:
            self.penup()
            self.goto(self.xcor(), -Y)
            self.pendown()
        

if __name__ == "__main__":
    print("Running.......")
    try:
        App = confused_lines()
        print("Closing screen")
    except Terminator:
        print("Forced Stop")
