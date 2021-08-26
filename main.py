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
        self.reg_players = ['HAL9000','VIKI']
        self.quit_game = False
        self.score_board = ''

    def run(self):
        # Intro text, only to be displayed on initial opening of game.
        print("Welcome to the World of Mastermind!")
        print("Developed by Mason Manuel")
        print("COMP 1048 UO Object-Oriented Programming")

        play_game = wom.options()
        if play_game:
            game = Game()
            game.setGParameters()



    def options(self):

        user_selection = ''

        # This loop validates user input
        while user_selection not in ['r', 's', 'p', 'q']:
            print()
            print("What would you like to do?")
            print(" (r) register a new user")
            print(" (s) show the score board")
            print(" (p) play a game")
            print(" (q) quit")
            user_selection = input('> ')

            # These if statements take user input and call the respected methods
            # to undertake each task.
            if user_selection == 'r':
                wom.registerPlayer()
                print("out of function")
                print(self.reg_players)

            elif user_selection == 's':
                wom.showScoreBoard()

            elif user_selection == 'q':
                print(self.quit_game)
                self.quit_game = wom.quitGame()
                print("out of function")
                print(self.quit_game)

            # There is no else statement here to cut down on duplicated code.
            # instead, next if statement will revert user_selection back to blank to
            # go to the top of the while loop to show the options text again.
            # if the selection was 'p', the game will progress to wom.playGame()

            if user_selection == 'p':
                return True
            else:
                user_selection = ''



    def playGame(self):
        print("Let’s play the game of Mastermind!")


    def quitGame(self):
        quit_game = True
        return quit_game

    def registerPlayer(self):
        new_player = input("What is the name of the new user?\n> ").capitalize()

        if new_player not in self.reg_players:
            self.reg_players.append(new_player)
            print("Welcome, " + new_player + '!')
        else:
            print("Sorry, the name is already taken.")

    def showScoreBoard(self):
        print("this is where the scoreboard goes")

class Players():

    def __init__(self):
        self.score = 0
        self.games = 0
        self.average = self.score / self.games

    class gamePlayers():

        def __init__(self, player_id):
            self.id = player_id
            self.score = 0

class Game():

    def __init__(self):
        self.n_players = 0
        self.n_guesses = 0

    def setGParameters(self):
        while self.n_players != [2-5]:
            self.n_players = int(input("How many players (2-4)?\n> "))
            if self.n_players != [2-5]:
                print("Number of players must be between 2-4")
            else:
                pass


        self.n_guesses = input("")

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

#class GamePiece(p_index, p_colour):

   # def __init__(self, p_index, p_colour):
       # self.position = p_index
        #self.colour = p_colour


    #class Peg():
     #   # def placePegs(code):
     #   pass

   # class Marbel():
      #  pass


wom = WorldOfMastermind()
wom.run()

