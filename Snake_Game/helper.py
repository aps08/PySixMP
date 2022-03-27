from encodings import utf_8
from turtle import Turtle
import random

class Snake:

    """
    Creates the snake on the screen and moves it forward. Also responsible for extending the snake and finding distance between
    required fields, like distnace between head and tail, and walls. 
    """

    def __init__(self) -> None:
        """ __init__() --> Contructor. For initializing some useful variables.
        """
        self.__SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        self.__MOVE_DISTANCE = 20
        self.__UP = 90
        self.__DOWN = 270
        self.__RIGHT = 0
        self.__LEFT = 180
        self.__segments = []
        self.create_snake()

    def create_snake(self) -> None:
        """ create_snake() --> creates the snake.
        """
        for tp in self.__SEGMENT_POSITIONS:
            self.add_segment(tp)

    def add_segment(self, position: tuple) -> None:
        """ add_segment() --> helper for creating snake.

        Args:
            position (tuple): stores co-ordinates of the segments.
        """
        Obj = Turtle(shape="square", visible=False)
        Obj.penup()
        Obj.color("green")
        Obj.goto(position)
        Obj.showturtle()
        self.__segments.append(Obj)

    def move_snake(self) -> None:
        """ move_snake() --> moves the snake by 20 units.
        """
        for seg in range(len(self.__segments) - 1, 0, -1):
            x = self.__segments[seg - 1].xcor()
            y = self.__segments[seg - 1].ycor()
            self.__segments[seg].color("lightgreen")
            self.__segments[seg].goto(x=x, y=y)
        self.__segments[0].forward(self.__MOVE_DISTANCE)

    def extend_snake(self) -> None:
        """ extend_snake() --> add a segment in snake if it eats the food.
        """
        self.add_segment(self.__segments[-1].position())

    def Up(self) -> None:
        """ up() --> function for moving snake using arrows keys.
        """
        if self.__segments[0].heading() != self.__DOWN:
            self.__segments[0].setheading(self.__UP)

    def Down(self) -> None:
        """ down() --> function for moving snake using arrows keys.
        """
        if self.__segments[0].heading() != self.__UP:
            self.__segments[0].setheading(self.__DOWN)

    def Left(self) -> None:
        """ left(), right() --> function for moving snake using arrows keys.
        """
        if self.__segments[0].heading() != self.__RIGHT:
            self.__segments[0].setheading(self.__LEFT)

    def Right(self) -> None:
        """ right() --> function for moving snake using arrows keys.
        """
        if self.__segments[0].heading() != self.__LEFT:
            self.__segments[0].setheading(self.__RIGHT)

    def get_segment(self) -> list:
        """ get_segment() --> return the segments.

        Returns:
            list: return the co-ordinates of the segment
        """
        return self.__segments

    def head_distance(self, Food_Obj: object) -> float:
        """ head_distance() --> returns the distance of head from food object.

        Args:
            Food_Obj (object): it is a object of Food class type

        Returns:
            float: return the distance between the food and the head of snake.
        """
        return self.__segments[0].distance(Food_Obj)

    def get_head_X(self) -> float:
        """ get_head_X() --> return the X co-ordinates for the head segment respectively.
        """
        return self.__segments[0].xcor()

    def get_head_Y(self) -> float:
        """ get_head_X(), get_head_Y() --> return the Y co-ordinates for the head segment respectively.
        """
        return self.__segments[0].ycor()

class Food(Turtle):
    """
    Create the food object on the screen, and repeast itself if the food is eaten by the snake.
    """

    def __init__(self) -> None:
        """  __init__() --> Contructor. Responsible for creating the first object on the screen.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.next_food()

    def next_food(self) -> None:
        """ next_food() --> creates the next food object, when the food has been eaten.
        """
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        

class ScoreBoard(Turtle):
    """
    Create the scoreboard on the screen the updates the score.
    """
    
    def __init__(self, highcore: int) -> None:
        """ __init__() --> Contructor. Responsible for creating the scoreboard on the screen and showing the score.

        Args:
            highcore (int): sotres the highscore
        """
        super().__init__()
        self.__score = -10
        self.__FONT = ("Courier", 12, "bold")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.write_score(highcore)

    def write_score(self, score: int) -> None:
        """ write_score() --> Write the scoreboard on the screen, and increase by 10, if snake eats the food.

        Args:
            score (int): stores the score
        """
        self.clear()
        self.__score += 10
        self.write(f'SCORE : {self.__score}\nHighest Score : {score}', move=False, align="Center", font=self.__FONT)

    def game_over(self) -> None:
        """ game_over() --> shows game over message once the game has ended.
        """
        self.goto(0, 0)
        self.write(f'GAME OVER YOUR SCORE WAS : {self.__score} \nClosing windows in 5 seconds', move=False, align="Center", font=self.__FONT)

    def get_score(self) -> int:
        """ get_score() --> returnt the score of the user.

        Returns:
            int: return the score of the user.
        """
        return self.__score

class Highscore:
    """
    This class is responsible for creating a file and updating the high score when actived by user. 
    """

    def __init__(self) -> None:
        """  __init__() --> Contructor. Create the file is not present and loads data, and get the high score if the file is presents.
        """
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
        """ get_highscore() --> return the highest score for comparison.

        Returns:
            int: return the highscore
        """
        return int(self._data)

    def update_score(self, highscore: int) -> None:
        """ update_score() --> overrides the highscore if new highscore is achieved.

        Args:
            highscore (int): stores high score
        """
        with open("Snake_Game/high_score.txt", mode="w", encoding="utf-8") as f:
            f.write(f'{highscore}')
            f.close()
