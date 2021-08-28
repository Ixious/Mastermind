#
# File: mastermind.py
# Descrition: this file is a text based version of the board game, mastermind.
# Author: Mason Manuel
# Student ID: 110120048
# Email ID: manmo001
# This is my own work as defined by
#  the University's Academic Misconduct Policy.
#
class WorldOfMastermind:

    def __init__(self):
        self.reg_players = ['HAL9000','VIKI']
        self.quit_game = False
        # self.score_board = ''

    def run(self):

        # Intro text, only to be displayed on initial opening of game.
        print("Welcome to the World of Mastermind!")
        print("Developed by Mason Manuel")
        print("COMP 1048 UO Object-Oriented Programming")

        # Initiates options screen, this is a while loop that only progresses
        # when wom.options returns bool True for play_game. (user selects play)
        play_game = wom.options()

        if play_game:

            game = Game()                       # Initializes Game object
            game.playerList(game.nPlayers())    # Populates the playerList and nPlayers in game object
            game.setGuesses()                   # Sets nGuesses

            # Creates a board for each player to host set code, code attempts etc.
            player_board = []
            for each_player in game.player_list:

                board = Board(each_player, game.n_guesses)
                player_board.append(board)

            # Codes can be set now that all the boards have been constructed with the above for loop.
            index = 0
            for each_player in game.player_list:

                if index < len(game.player_list) - 1:
                    print('\n* ', each_player, "'s turn to set the code for ", game.player_list[index + 1],
                          " to break.", sep='')

                    # index + 1 is next player. i.e. Player at index 0 sets for index 1, and so on.
                    player_board[index + 1].set_code = player_board[index + 1].setCode()
                    print("The code is now set for", game.player_list[index + 1], 'to break')

                elif index == len(game.player_list) - 1:
                    print('\n*', each_player, "'s turn to set the code for ", game.player_list[0],
                          " to break.", sep='')

                    # when index is same as len(), it's the last player, who needs to set code for index 0.
                    player_board[0].set_code = player_board[0].setCode()
                    print("The code is now set for", game.player_list[0], 'to break')

                index += 1

            for each_board in player_board:
                pdex = 0  # player index
                correct_guess = False

                while player_board[pdex].attempts_left > 0 and not correct_guess:
                    print('\n* ', each_board.breaker_name, "'s turn to guess the code.", sep='')
                    print("Previous attempts:", player_board[pdex].attempts_taken)
                    if player_board[pdex].attempts_taken > 0:
                        player_board[pdex].giveFeedback()
                    print("Attempts left:", player_board[pdex].attempts_left)

                    player_board[pdex].current_guess = player_board[pdex].setCode()
                    player_board[pdex].guess_log.append(player_board[pdex].current_guess)

                    if player_board[pdex].testGuess():
                        print("GOT THE RIGHT CODE MOTHERFUCKER")
                        correct_guess = True
                    elif not player_board[pdex].testGuess():
                        print("Feedback: ", end='')
                        print(player_board[pdex].feedback)

                    player_board[pdex].attempts_left -= 1
                    player_board[pdex].attempts_taken += 1

            pdex += 1

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
        new_player_name = input("What is the name of the new user?\n> ")

        if new_player_name not in self.reg_players:
            self.reg_players.append(new_player_name)
            print("Welcome, " + new_player_name + '!')
            new_player = Players()
            new_player.setName(new_player_name)
            print("TESTING", new_player.getName(), "'s score: " ,new_player.score)
        else:
            print("Sorry, the name is already taken.")

    def showScoreBoard(self):
        print("this is where the scoreboard goes")
        print("TESTING STILL IN DEVELOPMENT")

class Players:

    def __init__(self):
        self.score = 0
        self.games = 0
        self.name = ''

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    class gamePlayers():

        def __init__(self, player_id):
            self.id = player_id
            self.score = 0

class Game:

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

        index = 0

        for player_id in range(n_players):
            player_name = ''
            while player_name not in self.player_list:
                player_name = input("What is the name of player #" + str(index + 1) + "?\n> ")
                if player_name not in wom.reg_players:
                    print("Invalid user name.")
                elif player_name in self.player_list:
                    print(player_name," is already in the game.")
                    player_name =''
                else:
                    self.player_list.append(player_name)
            index += 1

    def setGuesses(self):

        while self.n_guesses not in range(5,11):

            self.n_guesses = input("How many attempts will be allowed for each player (5-10)?\n> ")
            if not self.n_guesses.isnumeric():
                print("Number must be between 5-10")
            else:
                self.n_guesses = int(self.n_guesses)

                if self.n_guesses not in range(5, 11):
                    print("Number must be between 5-10")

class Board:

    def __init__(self, player_name, n_guess):
        self.attempts_taken = 0
        self.attempts_left = n_guess
        self.set_code = ''
        self.current_guess = ''
        self.breaker_name = player_name
        self.guess_log = []
        self.feedback_log = []
        self.feedback = ''
        self.correct_guess = False

    def setCode(self):
        user_set_code = Code()
        user_set_code.setInputCode()
        return user_set_code.getInputCode()

    def testGuess(self):

        # Initial check to bypasss computations in case guess = correct
        if self.current_guess == self.set_code:
            return True
        else:
            # Resets feedback to blank, previous feedback is now stored in feedback_log
            self.feedback = ''
            new_list = []

            for char in self.set_code:
                new_list.append(char)

            marble_index = 0
            for marble in self.current_guess:

                if marble == self.set_code[marble_index]:
                    self.feedback += 'K '
                    del new_list[new_list.index(marble)]
                marble_index += 1

            for marble in self.current_guess:
                if marble in new_list:
                    self.feedback += 'W '
                    new_list.remove(marble)
                marble_index += 1

            self.feedback_log.append(self.feedback)
            return False

    def giveResult(self):
        pass

    def giveFeedback(self):
        feedback_index = 0

        print("==============")
        print("Code Feedback")
        print("==============")
        for each_score in self.guess_log:
            print(str(each_score), end='')
            print(str(self.feedback_log[feedback_index]))
            feedback_index += 1
        print("==============")

    def tallyScore(self):
        pass

    pass

class Code:

    def __init__(self):
        self.input_code = ''

    def setInputCode(self):

        allowable_colours = ['R', 'G', 'B', 'Y', 'W', 'K']

        while len(self.input_code) != 4:
            self.input_code = input('Please enter the code:\n> ').upper()
            if len(self.input_code) != 4:
                print("Invalid code.")
                print("It must be exactly four characters, each can be R, G, B, Y, W, or K. ")
                self.input_code = 'ERRORFOUND'
            else:
                error_present = False
                for marble in self.input_code:
                    if marble not in allowable_colours:
                        error_present = True
                if error_present:
                    print("Invalid code.")
                    print("It must be exactly four characters, each can be R, G, B, Y, W, or K. ")
                    self.input_code = 'ERRORFOUND'

    def getInputCode(self):
        return self.input_code


class GamePiece:

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

