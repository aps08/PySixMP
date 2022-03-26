from turtle import Turtle, Screen, numinput
import random
import time
import constants as C
"""
This file contains import statements and some constants which you could use to customize interface and functionality of this code.
Before reading further, I suggest you to run the code and see how it works.
"""

# Title of the screen
TITEL_TEXT = "Confused Lines! 😉😉😉😉"
# Background Colour of the screen
BG_COLOR = "black"
# Start pen color
PEN_COLOR = "white"
# Sleep Time, after how much time the screen should close. In seconds
SLEEP_TIME = 3
# Instruction which you see at the top of screen, on start of the program.
INSTRUCTION_TEXT = "Window will close automatically after it's done"
# Instruction which you see at the end of program.
END_INSTRUCTION_TEXT = "Closing window in 3 seconds"
# This text is shown, when you are prompted to Enter, how many time you want the lines to run. By default it's value is 50. 
PROMPT_TEXT = "Enter number of times you want to run the lines.\nDefault value:50"
# Font which you see on the screen.
FONT = ("Courier", 12, "bold")
# X co-ordinates for the start of the line. Hortizaontal
X = 400.0
# Y co-ordinates for the start of the line. Vertical
Y = 300.0
# Angles at which the lines can you. A random value will be select from this list.
ANGLES = [0, 90, 180, 270]
# Distance which will be convered for each turn. A random value will selected after each turn.
FORWARD_BY = [50, 100]
# Thickness of the line.
PENSIZE = 10