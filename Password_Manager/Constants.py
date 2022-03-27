from tkinter import *
from tkinter import messagebox, simpledialog
import random
import validators
import pyperclip
import json
import sys

"""
This file contains import statements and some constants which you could use to customize interface and functionality of this code.
Before reading further, I suggest you to run the code and see how it works.
"""

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPER_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '}']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
LIST = [LETTERS, NUMBERS, SYMBOLS, UPPER_LETTERS]
FONT = ("Veradana", 8, "bold")
TITLE = "Password Manager! 🔓🔓🔓"
BG_COLOR = "lightgrey"
LOGO_PATH = r"Password_Manager\_assets\logo.png"
FILE_PATH = r"Password_Manager\_assets\user_data.json"
EMAIL_ERROR = "Doesn't look like a email. Try again."
DOMAIN_ERROR = "Doesn't look like a domain. Try again."
DOMAIN_EXISTS_ERROR = "Domain already exists in the password manager."
SAVE_SUCCESS = "Details and Password saved successfully."
NO_DATA = "No data found for that domain."
SUCCESS_GET = "Email and Password for the searched domain has been populated."
PASSWORD_COPY = "Password has been copied to your clipboard."
LENGTH_ERROR = "Number must be greater than 8 and less than 26."
# Put your default email here
DEFAULT_EMAIL = "defaultemail@gmail.com"