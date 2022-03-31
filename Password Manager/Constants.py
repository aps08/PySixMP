from tkinter import *
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
from typing import Union
import random
import validators
import pyperclip
import json
import sys
import os

"""
This file contains import statements and some constants which you could use to customize interface and functionality of this code.
Before reading further, I suggest you to run the code and see how it works.
"""

# Put your default email here
DEFAULT_EMAIL = "defaultemail@gmail.com"
# Lower case letters for random password
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Upper case letters for random password
UPPER_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Different Symbols for random password
SYMBOLS = ['#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '}']
# Digits for random password
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# A List of all the above list for random password
LIST = [LETTERS, NUMBERS, SYMBOLS, UPPER_LETTERS]
# Font size and style for texts.
FONT = ("Veradana", 8, "bold")
# Title of the windows which appears at run time.
TITLE = "Password Manager! 🔓🔓🔓"
# backgorund color
BG_COLOR = "lightgrey"
# Path for Logo
LOGO_PATH = r"Password Manager\_assets\logo.png"
# Path for json file
FILE_PATH = r"Password Manager\_assets\user_data.json"
# Path for secret key file
SECRET_KEY_PATH = r"Password Manager\_assets\secret.key"
# Error message if email is not valid.
EMAIL_ERROR = "Doesn't look like a email. Try again."
# Error message if domain is not valid.
DOMAIN_ERROR = "Doesn't look like a domain. Try again."
# Error message if domain already exists in the password manager.
DOMAIN_EXISTS_ERROR = "Domain already exists in the password manager."
# Success message if data is saved.
SAVE_SUCCESS = "Details and Password saved successfully."
# Error message if no data is found for a domain.
NO_DATA = "No data found for that domain."
# Success message for search.
SUCCESS_GET = "Email and Password for the searched domain has been populated."
# Info message when password is generated successfully.
PASSWORD_COPY = "Password has been copied to your clipboard."
# Error message if password length is not in limit.
LENGTH_ERROR = "Number must be greater than 8 and less than 99."