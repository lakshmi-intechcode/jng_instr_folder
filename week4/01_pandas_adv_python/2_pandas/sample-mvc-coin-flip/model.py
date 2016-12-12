'''
model.py

I handle the application's logic and manipulation of data.
'''
from random import randint

class Game:
    def flip(self, guess):
        if guess == str(randint(1,2)):
            return True
        return False

if __name__ == "__main__":
    g = Game()
    x = g.flip('1'); print(x)
