'''
controller.py

To run the application, run this file.
'''
from model import Game
from view import View

if __name__ == '__main__':
    g = Game()
    v = View()

    quit = False

    while not quit:
        choice = v.prompt()
        if choice in ['1', '2']:
            v.result(g.flip(choice))
        else:
            quit = True
