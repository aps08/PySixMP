import constants as C

class confused_lines(C.Turtle):
    """
    Summary of the class:
    This class is responsible for runnig the confused lines and inherits the turtle object.

    Funcions and uses:
    1. __init__() --> Constructor. Creates the screen and takes the input from user.
    2. write_instructions() --> responsible for showing text on the screen.
    3. run() --> run the loop N times, which is taken from the user, by default the value is 50.
    4. mirror() --> responsible for mirroring the turtle, on the opposite side of the wall.
    """

    def __init__(self) -> None:
        super().__init__()
        self.screen = C.Screen()
        self.screen.cv._rootwindow.resizable(False, False)
        self.screen.title(C.TITEL_TEXT)
        self.screen.bgcolor(C.BG_COLOR)
        self.screen.setup(width=int(C.X)*2, height=int(C.Y)*2)
        self.write_instruction()
        self.input = int(C.numinput(title="Number", prompt=C.PROMPT_TEXT, default=50,minval=50, maxval=9999))
        self.run()

    def write_instruction(self) -> None:
        self.hideturtle()
        self.pensize(C.PENSIZE)
        self.penup()
        self.goto(x=0, y= int(C.Y)-40)
        self.pendown()
        self.pencolor(C.PEN_COLOR)
        self.write(C.INSTRUCTION_TEXT, align="center", font=(C.FONT))
        self.penup()
        self.home()
        self.pendown()

    def run(self) -> None:
        for i in range(self.input):
            self.mirror()
            self.color(['#%06X' % C.random.randint(0, 0xFFFFFF) for i in range(1)][0])
            self.right(C.random.choice(C.ANGLES))
            self.forward(C.random.choice(C.FORWARD_BY))
        self.clear()
        self.penup()
        self.home()
        self.pendown()
        self.pencolor(C.PEN_COLOR)
        self.write(C.END_INSTRUCTION_TEXT, align="center", font=C.FONT)
        C.time.sleep(C.SLEEP_TIME)

    def mirror(self) -> None:
        if self.xcor() < -C.X:
            self.penup()
            self.goto(C.X, self.ycor())
            self.pendown()
        if self.xcor() > C.X:
            self.penup()
            self.goto(-C.X, self.ycor())
            self.pendown()
        if self.ycor() < -C.Y:
            self.penup()
            self.goto(self.xcor(), C.Y)
            self.pendown()
        if self.ycor() > C.Y:
            self.penup()
            self.goto(self.xcor(), -C.Y)
            self.pendown()
        

if __name__ == "__main__":
    print("Running.......")
    try:
        App = confused_lines()
        print("Closing screen")
    except:
        print("Forced Stop")
