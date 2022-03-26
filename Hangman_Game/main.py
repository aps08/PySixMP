import random
from PyDictionary import PyDictionary
import os
import time
import msvcrt as m
import constants as C



class Hangman:
    def __init__(self) -> None:
        self._dictionary = PyDictionary()
        self._word = random.choice(C.WORD_LIST).lower()
        self._chances = ["💚"]*7
        self._blanks = [" _ "]*len(self._word)
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
                finally:
                    self._chances.pop()
        elif user_entry.isalpha():
            self.replace_blank(user_entry)
        if self._word.lower() == (''.join(self._blanks)).lower():
            self._clear()
            print(f"The word was {self._word.upper()}")
            print(f"You Won!!!! with {len(self._chances)} lives left.")
            self.retry()
                
                
    def replace_blank(self, user_entry: str) -> None:
        user_entry = user_entry.lower()
        if user_entry in self._used_alphabets:
            print("\nYou have already used this letter. Try again.")
            time.sleep(1)
        elif user_entry in self._word:
            for i in range(len(self._word)):
                if user_entry == self._word[i]:
                    self._blanks[i] = user_entry
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
            print(C.HANGMANPICS[7-len(self._chances)])
            print(f"\nLifes left : {self._chances}")
            print(f"Guess the word: {''.join(self._blanks)}")
            if self._used_alphabets:
                print(f"Used alhpabets : {self._used_alphabets} ")
            if self._give_hint:
                print(f'HINT: {self._give_hint}')
                print("Enter you alphabets here: ")
            else:
                print("Enter you alphabets here or 0 for a hint, which will reduce one life : ")
            user_guess = m.getwche()
            self.validate_anwer(user_guess)
            time.sleep(1)
        self.game_over()
        
    def game_over(self) -> None:
        self._clear
        print("Game over, all lifes lost. You are hanged.")
        print(f"The correct word was:  {self._word.upper()}")
        self.retry()
        
    def retry(self) -> None:
        print("Do you want to retry ?\n1. Y for YES\n2. Anyother key for NO")
        user_retry = m.getwche()
        self.__init__() if user_retry.upper() == "Y" else sys.exit(0)
    
if __name__ == "__main__":
    print("Starting the game...")
    H = Hangman()