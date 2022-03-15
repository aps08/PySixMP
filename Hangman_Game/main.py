import random
import sys
from PyDictionary import PyDictionary
import os
import time
import msvcrt as m

WORD_LIST = ['horse','door','song','rip','backbone','bomb','whisk','frog','lawnmower','mattress','pinwheel','cake','circus','battery','mailman','cowboy','password','bicycle',
        'skate','electricity','lightsaber','thief','teapot','deep','spring','nature','shallow','toast','outside','America','roller','blading','gingerbread','man','bowtie',
        'half','spare','wax','light','bulb','platypus','music''treasure','garbage','park','pirate','ski','state','whistle','palace','baseball','coal','queen','dominoes',
        'photograph','computer','hockey','aircraft','hot','dog','salt','pepper','key','iPad']

class Hangman:
    def __init__(self) -> None:
        self._dictionary = PyDictionary()
        self._word = random.choice(WORD_LIST).lower()
        self._chances = ["💚"]*7
        self._blanks = "_ "*len(self._word)
        self._clear = lambda: os.system('cls')
        self._used_alphabets = []
        self._give_hint = None
        self.instructions()
    
    def instructions(self) -> None:
        while True:
            self._clear()
            entry = ""
            print("\033[1;36;40mWelcome to Hangman Game......")
            print("........................................Instructions............................................")
            print("1. You will get 7 lifes to complete this game.")
            print("2. Number of 💚 shows how many lifes you have left.")
            print("3. On each correct guess, the letter will be added to the blank spaces at the correct position.")
            print("4. On each incorrect guess, you will lose a life.")
            print("4. You can only enter alphabets.")
            print("................................................................................................")
            print("Press 'P' to play the game.")
            print("Press 'Q' to quit the game.")
            print("ENTER YOUR CHOICE:")
            entry = m.getwche().upper()
            if entry in ['Q', 'P']:
                break
        sys.exit() if entry == 'Q' else self.start() if entry == 'P' else ''
        
    def validate_anwer(self, user_entry: str) -> None:
        if user_entry.isdigit() and self._give_hint is None:
            if user_entry == '0':
                try:
                    self._give_hint = self._dictionary.meaning(self._word)["Noun"][0]
                except:
                    self._give_hint = "No hint found."
        elif user_entry.isalpha():
            user_entry = user_entry.lower()
            if user_entry in self._used_alphabets:
                print("\nYou have already used this letter. Try again.")
                time.sleep(2)
            elif user_entry in self._word:
                for index, value in enumerate(self._word):
                    if user_entry == value:
                        self._blanks = self._blanks[0:index] + user_entry + self._blanks[index+1:]
                if user_entry not in self._used_alphabets:
                    self._used_alphabets.append(user_entry)
                print("\nCorrect guess.")
            else:
                if user_entry not in self._used_alphabets:
                    self._used_alphabets.append(user_entry)
                print("\nIncorrect. Life Lost ")
                self._chances.pop()
                            
        
    def start(self) -> None:
        while len(self._chances) > 0:
            self._clear()
            print(f"\nLifes left : {self._chances}")
            print(f"Guess the word: {self._blanks}")
            if self._used_alphabets:
                print(f"Used alhpabets : {self._used_alphabets} ")
            if self._give_hint:
                print(f'HINT: {self._give_hint}')
                print("Enter you alphabets here: ")
            else:
                print("Enter you alphabets here or 0 for a hint : ")
            user_guess = m.getwche()
            self.validate_anwer(user_guess)
            time.sleep(1)
        self.game_over()
        
    def game_over(self) -> None:
        print(self._word)
        print("Game over")
    
if __name__ == "__main__":
    print("Starting the game...")
    Hangman = Hangman()