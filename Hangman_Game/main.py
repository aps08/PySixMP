import random

WORD_LIST = ['horse','door','song','rip','backbone','bomb','whisk','frog','lawnmower','mattress','pinwheel','cake','circus','battery','mailman','cowboy','password','bicycle',
        'skate','electricity','lightsaber','thief','teapot','deep','spring','nature','shallow','toast','outside','America','roller','blading','gingerbread','man','bowtie',
        'half','spare','wax','light','bulb','platypus','music''treasure','garbage','park','pirate','ski','state','whistle','palace','baseball','coal','queen','dominoes',
        'photograph','computer','hockey','aircraft','hot','dog','salt','pepper','key','iPad']
CHANCES = 7

class Hangman:
    def __init__(self) -> None:
        self._word = random.choice(WORD_LIST)
        self._guess_word = ['*']*len(self._word)
        self._chances = CHANCES
        
    def start(self) -> None:
        pass
    
if __name__ == "__main":
    print("Starting the game...")
    Hangman.start()