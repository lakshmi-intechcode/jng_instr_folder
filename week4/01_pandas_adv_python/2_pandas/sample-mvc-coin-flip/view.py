'''
view.py

I present the application's interface and accept user input.
'''
class View:
    def prompt(self):
        valid = ['1', '2', '0']
        choice = None
        while choice not in valid:
            print()
            print('(1) HEADS')
            print('(2) TAILS')
            print('(0) QUIT')
            choice = input('Guess: ')
        return choice

    def result(self, user_won):
        if user_won:
            print('YOU WIN.')
        else:
            print('YOU LOSE.')
        return None


if __name__ == "__main__":
    v = View()
    v.prompt()
    v.result()
