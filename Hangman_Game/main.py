import constants as C


class Hangman:
    """
    This class is responsible for runnig the Hangman game.
    """
    def __init__(self) -> None:
        """ __init__() --> This is a construtor, which is responsible for creating objects and variables,
                            which will help us during the program.
        """ 
        self._dictionary = C.PyDictionary()
        self._word = C.random_word()
        self._chances = ["💚"]*C.LIFES
        self._blanks = [" _ "]*len(self._word)
        self._clear = lambda: C.os.system('cls')
        self._used_alphabets = []
        self._give_hint = None
        self.instructions()
    
    def instructions(self) -> None:
        """ instructions() --> This function is responsible for showing the menu of the game to user.
        """
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
            entry = C.m.getwche().upper()
            if entry in C.ENTRY:
                break
        C.sys.exit() if entry == C.ENTRY[0] else self.start() if entry == C.ENTRY[1] else ''
        
    def start(self) -> None:
        """ start() --> This function is responsible for running the game until you have lost all the lifes.
        """
        while len(self._chances) > 0:
            self._clear()
            print(C.HANGMANPICS[7-len(self._chances)])
            print(f"\nLifes left : {self._chances}")
            print(f"Guess the word: {''.join(self._blanks)}")
            if self._used_alphabets:
                print(f"Used alhpabets : {self._used_alphabets} ")
            if self._give_hint:
                print(f'HINT: {self._give_hint}')
                print(C.INSTRUCTION[0])
            else:
                print(C.INSTRUCTION[1])
            user_guess = C.m.getwche()
            self.validate_anwer(user_guess)
            C.time.sleep(1)
        self.retry()
        
    def validate_anwer(self, user_entry: str) -> None:
        """ validate_anwer() --> This fucntion is responsible for validating the user input. 
        
        Args:
            user_entry (str): This argument keep the value of user's guessed letter,
                              on which the validation ips performed.
        """
        if user_entry.isdigit() and self._give_hint is None:
            if user_entry == '0':
                try:
                    self._give_hint = self._dictionary.meaning(self._word)["Noun"][0]
                except IndexError:
                    self._give_hint = C.NO_HINT_FOUND
                except:
                    self._give_hint = C.NO_HINT_FOUND
                finally:
                    self._chances.pop()
        elif user_entry.isalpha():
            self.replace_blank(user_entry)
        if self._word.lower() == (''.join(self._blanks)).lower():
            self._clear()
            print(C.WON_TEXT.format(len(self._chances)))
            self.retry()
                
                
    def replace_blank(self, user_entry: str) -> None:
        """ replace_blank() --> This function is responsible for replacing the blank wih correct letter,
                                if the validation result is true.
        Args:
            user_entry (str): This argument keep the value of user's guessed letter,
                              on which the validation is performed.
        """
        user_entry = user_entry.lower()
        if user_entry in self._used_alphabets:
            print(C.USED_TEXT)
            C.time.sleep(1)
        elif user_entry in self._word:
            for i in range(len(self._word)):
                if user_entry == self._word[i]:
                    self._blanks[i] = " "+user_entry+" "
            if user_entry not in self._used_alphabets:
                self._used_alphabets.append(user_entry)
            print(C.CORRECT_INCORRECT[0])
        else:
            if user_entry not in self._used_alphabets:
                self._used_alphabets.append(user_entry)
            print(C.CORRECT_INCORRECT[1])
            self._chances.pop()                       
        
        
    def retry(self) -> None:
        """ retry() --> This function is responsible for checking if the user wants to play again or not, 
                        it also shows the correct answers.
        """
        self._clear()
        print(C.GO_INSTRUCTION)
        print(f"The correct word was:  {self._word.upper()}")
        print("\n\n")
        print(C.RETRY_INSTRUCTION)
        user_retry = C.m.getwche()
        self.__init__() if user_retry.upper() == "Y" else C.sys.exit(0)
    
if __name__ == "__main__":
    print("Starting the game...")
    H = Hangman()