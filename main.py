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

            n_players = int(wom.nPlayers())
            player_list = wom.playerList(n_players)
            n_guesses = int(wom.nGuesses())

            game = Game()
            game.__init__(n_players, player_list, n_guesses)



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

    def nPlayers(self):
        print("Let’s play the game of Mastermind!")
        n_players = 0

        while n_players not in range(2,5):
            n_players = int(input("How many players (2-4)?\n> "))
            if n_players not in range(2,5):
                print("Number of players must be between 2-4")
            else:
                return n_players



    def playerList(self, n_players):

        player_list = []
        index = 1
        for player_id in range(n_players):
            player_name = ''
            while player_name not in self.reg_players:
                player_name = input("What is the name of player #" + str(index) + "?\n> ")
                if player_name not in self.reg_players:
                    print("Invalid user name.")
                elif player_name in player_list:
                    print(player_name," is already in the game.")
                    player_name =''
            index += 1
            player_list.append(player_name)
        print(self.reg_players, ">>> registered players")
        print(player_list, ">>> player list for this game")



    def nGuesses(self):

        n_guesses = 0
        while n_guesses not in range(5,11):
            n_guesses = int(input("How many attempts will be allowed for each player (5-10)?\n> "))
            if n_guesses not in range(5,11):
                print("Number must be between 5-10")
        return n_guesses

    def quitGame(self):
        quit_game = True
        return quit_game

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

class Players():

    def __init__(self):
        self.score = 0
        self.games = 0

    class gamePlayers():

        def __init__(self, player_id):
            self.id = player_id
            self.score = 0

class Game():

    def __init__(self, n_players, player_list, n_guesses):
        self.n_players = n_players
        self.n_guesses = n_guesses
        self.player_list = player_list



    def gSetUp(self):

        print("Let’s play the game of Mastermind!")




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

