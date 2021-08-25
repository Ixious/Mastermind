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
        self.quit_game = False
        self.score_board = ''

    def run(self):
        print("Welcome to the World of Mastermind!")
        print("Developed by Mason Manuel")
        print("COMP 1048 UO Object-Oriented Programming")
        wom.options()
        print("out of wom.options")
        pass

    def options(self):

        user_selection = ''

        while user_selection != 'p':

            while user_selection not in ['r', 's', 'p', 'q']:
                print()
                print("What would you like to do?")
                print(" (r) register a new user")
                print(" (s) show the score board")
                print(" (p) play a game")
                print(" (q) quit")
                user_selection = input('> ')

            if user_selection == 'r':
                wom.registerPlayer()
                print("out of function")
                print(self.reg_players)

            elif user_selection == 's':
                wom.showScoreBoard()
            elif user_selection == 'p':
                wom.playGame()
            else:
                print(self.quit_game)
                self.quit_game = wom.quitGame()
                print("out of function")
                print(self.quit_game)

            user_selection = ''


    def playGame(self):
        pass

    def quitGame(self):
        quit_game = True
        return quit_game

    def registerPlayer(self):
        print("in registerPlayer")
        new_player = input("What is the name of the new user?\n> ").capitalize()

        if new_player not in self.reg_players:
            self.reg_players.append(new_player)
            print("Welcome, " + new_player + '!')
        else:
            print("Sorry, the name is already taken.")

    def showScoreBoard(self):
        print("this is where the scoreboard goes")


class Game():

    def __init__(self):
        self.n_players = 0
        self.n_guesses = 0

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

