#
# File: mastermind.py
# Descrition: this file is a text based version of the board game, mastermind.
# Author: Mason Manuel
# Student ID: 110120048
# Email ID: manmo001
# This is my own work as defined by
#  the University's Academic Misconduct Policy.
#
class WorldOfMastermind():

    def __init__(self):
        self.reg_players = []


    def run(self):
        pass

    def options(self):

        user_selection = ''

        while user_selection not in ['r', 's', 'p', 'q']:
            print("What would you like to do?")
            print(" (r) register a new user")
            print(" (s) show the score board")
            print(" (p) play a game")
            print(" (q) quit")
            user_selection = input()

        if user_selection == 'r':
            wom.registerPlayer()


    # def playGame():
    #   pass
    # def quitGame():
    #   pass
    def registerPlayer(self):
        print("in registerPlayer")
    #   pass
    # def showScoreBoard():
    #   pass

class Game():
    n_players = 0

    # setNGuesses():
    # setNPlayers():
    # checkPlayerName():
    pass

class Board():

    def __init__(self, n_guess, n_attempts):
        self.n_allowed_guesses = n_guess
        self.n_attempts = n_attempts

    code_guess = ""
    guess_log = "" #+ end line, + seps etc.
    feedback_list =[]

    def giveFeedback(self):
        pass
        #return #feedback

    def testGuess(self):

        # if code guess != set code:
        #   for marbel in code guess:
        #       if marbel == set code [index] and marbel == set code[colour]
        #           place colour
        #       if marbel == set code [colour] and != set code [index]:
        #           place colour for this result
        #return feedback_list
        pass

    def giveResult(self):
        pass

    def tallyScore(self):
        pass

    pass

class Code():
    #input_code = ""

    #inputCode():
    pass

class GamePiece():

    def __init__(self):
        self.position = p_index
        self.colour = p_colour


    class Peg():
        # def placePegs(code):
        pass

    class Marbel():
        pass


wom = WorldOfMastermind()
wom.run()
wom.options()

