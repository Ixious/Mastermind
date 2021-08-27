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

        # Initiates options screen, this is a while loop that only progresses
        # when wom.options returns bool True for play_game. (user selects play)
        play_game = wom.options()
        if play_game:
            game = Game()
            game.playerList(game.nPlayers())
            game.nGuesses()

            for each_player in game.player_list:
                each_player = Board()
                each_player.

    for each player in player list:
        print("* ", each_player, "'s turn to set the code for", next_player, "to break.")
        code.set



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

    def quitGame(self):
        quit_game = True
        return quit_game
        print("TESTING STILL IN DEVELOPMENT")

    def registerPlayer(self):
        new_player = input("What is the name of the new user?\n> ")

        if new_player not in self.reg_players:
            self.reg_players.append(new_player)
            print("Welcome, " + new_player + '!')
            new_player = Players()
        else:
            print("Sorry, the name is already taken.")

    def showScoreBoard(self):
        print("this is where the scoreboard goes")
        print("TESTING STILL IN DEVELOPMENT")

class Players():

    def __init__(self):
        self.score = 0
        self.games = 0

    class gamePlayers():

        def __init__(self, player_id):
            self.id = player_id
            self.score = 0

class Game():

    def __init__(self):
        self.n_players = 0
        self.n_guesses = 0
        self.player_list = []

    def nPlayers(self):
        print("Let’s play the game of Mastermind!")

        while self.n_players not in range(2,5):
            self.n_players = input("How many players (2-4)?\n> ")

            if not self.n_players.isnumeric():
                print("Number of players must be between 2-4")
                print("TESTING is numeric?", self.n_players.isnumeric())
            else:
                self.n_players = int(self.n_players)

                if self.n_players not in range(2,5):
                    print("Number of players must be between 2-4")

        return self.n_players

    def playerList(self, n_players):

        index = 1

        for player_id in range(n_players):
            player_name = ''
            while player_name not in self.player_list:
                player_name = input("What is the name of player #" + str(index) + "?\n> ")
                if player_name not in wom.reg_players:
                    print("Invalid user name.")
                elif player_name in self.player_list:
                    print(player_name," is already in the game.")
                    player_name =''

                self.player_list.append(player_name)

            index += 1

    def nGuesses(self):

        while self.n_guesses not in range(5,11):

            self.n_guesses = input("How many attempts will be allowed for each player (5-10)?\n> ")
            if not self.n_guesses.isnumeric():
                print("Number must be between 5-10")
            else:
                self.n_guesses = int(self.n_guesses)

                if self.n_guesses not in range(5, 11):
                    print("Number must be between 5-10")


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

        feedback_list = []

        if code_guess != set_code:
            for marble in code_guess:
                if marble == set_code[0]:
                    feedback_list.append('K')
                if marble != set_code[0] and marble in set_code:
                    feedback_list.append('W')

        return feedback_list

    def giveResult(self):
        pass

    def tallyScore(self):
        pass

    pass

class Code():

    allowable_colours = ['R', 'G', 'B', 'Y', 'W', 'K']
    set_code = ''

    while len(set_code) != 4:
        set_code = input('Please enter the code:\n> ').upper()
        if len(set_code) != 4:
            print("Invalid code.")
            print("It must be exactly four characters, each can be R, G, B, Y, W, or K. ")
            set_code = ''
        else:
            error_present = False
            for marble in set_code:
                if marble not in allowable_colours:
                    error_present = True
            if error_present:
                print("Invalid code.")
                print("It must be exactly four characters, each can be R, G, B, Y, W, or K. ")
                set_code = 'ERRORFOUND'

        print(set_code)

    print("The code is now set for ", 'next_player, to break')



class GamePiece(p_index, p_colour):

    def __init__(self, p_index, p_colour):
        self.position = p_index
        self.colour = p_colour

    class Peg():
        def placePegs(code):
            pass

    class Marbel():
        pass


wom = WorldOfMastermind()
wom.run()

