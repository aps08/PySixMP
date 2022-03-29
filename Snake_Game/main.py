from turtle import Screen, Terminator
from helper import Snake, ScoreBoard, Food, Highscore
import time


class Snake_Game:

    def __init__(self) -> None:
        """  __init__() --> Contructor. Create the screen and initialises all the object such as food, snake and scoreboard.
                            It is also responsible for creating the interface for playing the game. 
        """
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("grey")
        self.screen.setup(height=600, width=600)
        self.snake_segments = []
        self.game_on = True
        self.Snake = Snake()
        self.Food = Food()
        self.Highscore = Highscore()
        self._High = int(self.Highscore.get_highscore())
        self.ScoreBoard = ScoreBoard(self._High)
        self.screen.listen()
        self.screen.onkey(fun=self.Snake.Up, key="Up")
        self.screen.onkey(fun=self.Snake.Down, key="Down")
        self.screen.onkey(fun=self.Snake.Left, key="Left")
        self.screen.onkey(fun=self.Snake.Right, key="Right")
        self.run()

    def run(self) -> None:
        """ run() -->This function Contains the logic of the game. This function uses all the functions define in helper file,
                    to run the game. Some of the function call includes food, score, game over.
        """
        while self.game_on:
            self.screen.update()
            time.sleep(0.07)
            self.Snake.move_snake()

            if self.Snake.head_distance(self.Food) < 15:
                self.Food.next_food()
                self.ScoreBoard.write_score(self._High)
                self.Snake.extend_snake()

            if (self.Snake.get_head_X() > 280 or self.Snake.get_head_X() < -280) or (
                    self.Snake.get_head_Y() > 280 or self.Snake.get_head_Y() < -280):
                if self.ScoreBoard.get_score() > self._High:
                    self.Highscore.update_score(self.ScoreBoard.get_score())
                    self.ScoreBoard.clear()
                    self.ScoreBoard.home()
                    self.ScoreBoard.write("New high score", align="center", font=("Courier", 12, "bold"))
                    time.sleep(2)
                    self.ScoreBoard.clear()
                self.ScoreBoard.game_over()
                self.game_on = False

            for seg in self.Snake.get_segment()[1:]:
                if self.Snake.get_segment()[0].distance(seg) <10:
                    if self.ScoreBoard.get_score() > self._High:
                        self.Highscore.update_score(self.ScoreBoard.get_score())
                        self.ScoreBoard.clear()
                        self.ScoreBoard.home()
                        self.ScoreBoard.write("New high score", align="center", font=("Courier", 12, "bold"))
                        time.sleep(2)
                        self.ScoreBoard.clear()
                    self.game_on = False
                    self.ScoreBoard.game_over()

        time.sleep(5)
        self.screen.bye()

if __name__ == "__main__":
    print("Running...")
    try:
        Snake = Snake_Game()
        print("Closing screen")
    except Terminator:
        print("Forced Stop")
