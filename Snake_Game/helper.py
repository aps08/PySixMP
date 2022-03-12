from encodings import utf_8
from turtle import Turtle
import random

class Snake:

    """
    Summary of the class:
    Creates the snake on the screen and moves it forward. Also responsible for extending the snake and finding distance between
    required fields, like distnace between head and tail, and walls.

    Funcions and uses:
    1. __init__ --> Contructor.
    2. create_snake() --> creates the snake.
    3. add_segment() --> helper for creating snake.
    4. move_snake() --> moves the snake by 20 units.
    5. extend_snake() --> add a segment in snake if it eats the food.
    6. up(), down(), left(), right() --> function for moving snake using arrows keys.
    7. get_segment() --> return the segments.
    8. head_distance() --> returns the distance of head from food object.
    9. get_head_X(), get_head_Y() --> return the X and Y co-ordinates for the head segment respectively.
    """

    def __init__(self) -> None:
        self.__SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        self.__MOVE_DISTANCE = 20
        self.__UP = 90
        self.__DOWN = 270
        self.__RIGHT = 0
        self.__LEFT = 180
        self.__segments = []
        self.create_snake()

    def create_snake(self) -> None:
        for tp in self.__SEGMENT_POSITIONS:
            self.add_segment(tp)

    def add_segment(self, position: tuple) -> None:
        Obj = Turtle(shape="square", visible=False)
        Obj.penup()
        Obj.color("green")
        Obj.goto(position)
        Obj.showturtle()
        self.__segments.append(Obj)

    def move_snake(self) -> None:
        for seg in range(len(self.__segments) - 1, 0, -1):
            x = self.__segments[seg - 1].xcor()
            y = self.__segments[seg - 1].ycor()
            self.__segments[seg].color("lightgreen")
            self.__segments[seg].goto(x=x, y=y)
        self.__segments[0].forward(self.__MOVE_DISTANCE)

    def extend_snake(self) -> None:
        self.add_segment(self.__segments[-1].position())

    def Up(self) -> None:
        if self.__segments[0].heading() != self.__DOWN:
            self.__segments[0].setheading(self.__UP)

    def Down(self) -> None:
        if self.__segments[0].heading() != self.__UP:
            self.__segments[0].setheading(self.__DOWN)

    def Left(self) -> None:
        if self.__segments[0].heading() != self.__RIGHT:
            self.__segments[0].setheading(self.__LEFT)

    def Right(self) -> None:
        if self.__segments[0].heading() != self.__LEFT:
            self.__segments[0].setheading(self.__RIGHT)

    def get_segment(self) -> list:
        return self.__segments

    def head_distance(self, Food_Obj: object) -> float:
        return self.__segments[0].distance(Food_Obj)

    def get_head_X(self) -> float:
        return self.__segments[0].xcor()

    def get_head_Y(self) -> float:
        return self.__segments[0].ycor()

class Food(Turtle):
    """
    Summary of the class:
    Create the food object on the screen, and repeast itself if the food is eaten by the snake.

    Funcions and uses:
    1. __init__ --> Contructor.
    2. next_food() --> creates the next food object, when the food has been eaten.
    """

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.next_food()

    def next_food(self) -> None:
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        

class ScoreBoard(Turtle):
    """
    Summary of the class:
    Create the scoreboard on the screen the updates the score.

    Funcions and uses:
    1. __init__ --> Contructor.
    2. write_score() --> Write the scoreboard on the screen.
    3. game_over() --> shows game over message once the game has ended.
    4. get_score() --> returnt the score of the user.
    """
    
    def __init__(self, highcore: int) -> None:
        super().__init__()
        self.__score = -10
        self.__FONT = ("Courier", 12, "bold")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.write_score(highcore)

    def write_score(self, score: int) -> None:
        self.clear()
        self.__score += 10
        self.write(f'SCORE : {self.__score}\nHighest Score : {score}', move=False, align="Center", font=self.__FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f'GAME OVER YOUR SCORE WAS : {self.__score} \nClosing windows in 5 seconds', move=False, align="Center", font=self.__FONT)

    def get_score(self) -> None:
        return self.__score

class Highscore:
    """
    Summary of the class:
    This class is responsible for creating a file and updating the high score when actived by user. 

    Funcions and uses:
    1. __init__ --> Contructor. Create the file is not present and loads data, and get the high score if the file is presents.
    2. get_highscore() --> return the highest score for comparison.
    3. update_score() --> overrides the highscore if new highscore is achieved.
    """

    def __init__(self) -> None:
        self._data = None
        try :
            with open("Snake_Game/high_score.txt", mode="r", encoding="utf-8") as f:
                self._data = f.read()
        except :
            with open("Snake_Game/high_score.txt", mode="w+", encoding="utf-8") as f:
                f.write("50")
                self._data = 50
        f.close()
        
    def get_highscore(self) -> int:
        return int(self._data)

    def update_score(self, highscore: int) -> None:
        with open("Snake_Game/high_score.txt", mode="w", encoding="utf-8") as f:
            f.write(f'{highscore}')
            f.close()
