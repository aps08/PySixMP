# SOME CONSTANTS
LETTERS = [i for i in 'abcdefghijklmnopqrstuvwxyz']
UPPER_LETTERS = [i for i in 'abcdefghijklmnopqrstuvwxyz'.upper()]
NUMBERS = [i for i in "123456789"]
SYMBOLS = [i for i in "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"]
LIST = [LETTERS, NUMBERS, SYMBOLS, UPPER_LETTERS]
FONT = ("Veradana", 8, "bold")
TITLE = "Password Manager! 🔓🔓🔓"
BG_COLOR = "lightgrey"
LOGO_PATH = r"Password_Manager\_assets\logo.png"
FILE_PATH = r"Password_Manager\_assets\user_data.json"
DEFAULT_EMAIL = "defaultemail@gmail.com"
EMAIL_ERROR = "Doesn't look like a email. Try again."
DOMAIN_ERROR = "Doesn't look like a domain. Try again."
DOMAIN_EXISTS_ERROR = "Domain already exists in the password manager."
SAVE_SUCCESS = "Details and Password saved successfully."
NO_DATA = "No data found for that domain."
SUCCESS_GET = "Email and Password for the searched domain has been populated."
PASSWORD_COPY = "Password has been copied to your clipboard."
LENGTH_ERROR = "Number must be greater than 8 and less than 26."