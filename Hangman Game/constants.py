import random
from random_word import RandomWords
from PyDictionary import PyDictionary
import os
import time
import msvcrt as m
import sys
import re

"""
This file contains import statements and some constants which you could use to customize interface and functionality of this code.
Before reading further, I suggest you to run the code and see how it works.
"""

# Object for random world class
WORD_OBJECT = RandomWords()
# return random word
def random_word() -> str:
  result = False
  random_word = WORD_OBJECT.get_random_word()
  regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]-')
  try:
    if regex.search(random_word) == None:
      result = True
  except:
    result = False
  if result and random_word is not None and len(random_word) > 2:
    return random_word
  else:
    random_word()

# Number of lifes, incase you increase the number of lifes, please increate the graphics of HANGMANPICS variable.
LIFES = 7
# If no hint is found from the dictionary
NO_HINT_FOUND = "No hints, found"
# Text which is shown on winning
WON_TEXT = "You Won!!!! with {} lives left."
# Already used character warning
USED_TEXT = "\nYou have already used this letter. Try again."
# Instruction for entering value to proceed, with or without hint.
INSTRUCTION = ["Enter you alphabets here: " ,"Enter you alphabets here or 0 for a hint, which will reduce one life : "]
# Instruction for game over
GO_INSTRUCTION = "Game over, all lifes lost. You will be hanged."
# Retry instruction
RETRY_INSTRUCTION = "Do you want to retry ?\n1. Y for YES\n2. Anyother key for NO"
# Text for correct and incorrect gues
CORRECT_INCORRECT = ["\nCorrect guess.", "\nIncorrect guess. Life Lost "]
# ENTRIES
ENTRY = ['Q', 'P']
# This variable is used to show representation of the lifes lost.
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']