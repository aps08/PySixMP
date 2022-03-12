from turtle import Screen
from helper import Snake, ScoreBoard, Food
import time



screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(height=600, width=600)
snake_segments = []
game_on = True

Snake = Snake()
Food = Food()
ScoreBoard = ScoreBoard()

screen.listen()
screen.onkey(fun=Snake.Up, key="Up")
screen.onkey(fun=Snake.Down, key="Down")
screen.onkey(fun=Snake.Left, key="Left")
screen.onkey(fun=Snake.Right, key="Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    Snake.move_snake()

    if Snake.head_distance(Food) < 15:
        Food.next_food()
        ScoreBoard.write_score()
        Snake.extend_snake()

    if (Snake.get_head_X() > 280 or Snake.get_head_X() < -280) or (
            Snake.get_head_Y() > 280 or Snake.get_head_Y() < -280):
        ScoreBoard.game_over()
        game_on = False

    for seg in Snake.get_segment()[1:]:
        if Snake.get_segment()[0].distance(seg) <10:
            game_on = False
            ScoreBoard.game_over()

time.sleep(3)
screen.bye()

if __name__ == "__main":
    print("Running...")