#
# File: mastermind.py
# Descrition: this file is a text based version of the board game, mastermind.
# Author: Mason Manuel
# Student ID: 110120048
# Email ID: manmo001
# This is my own work as defined by
#  the University's Academic Misconduct Policy.
#

import random

class WorldOfMastermind:

    def __init__(self):
        self.cpu_players = ['HAL9000','VIKI']
        self.humans = []
        self.reg_players = []
        self.player_board = []
        self.quit_game = False
        # self.score_board = ''

    def run(self):

        # Intro text, only to be displayed on initial opening of game.
        print("Welcome to the World of Mastermind!")
        print("Developed by Mason Manuel")
        print("COMP 1048 UO Object-Oriented Programming")

        # Initiates options screen, this is a while loop that only progresses
        # when wom.options returns bool True for play_game. (user selects play)
        wom.options()

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
            user_selection = input('> ').lower()

            # These if statements take user input and call the respected methods
            # to undertake each task.
            if user_selection == 'r':
                wom.registerPlayer()

            elif user_selection == 's':
                wom.showScoreBoard()

            elif user_selection == 'q':
                wom.quitGame()

            elif user_selection == 'p':
                wom.playGame()

            if not wom.quit_game:
                user_selection = ''

    def playGame(self):

        game = Game()                     # Initializes Game object
        game.playerList(game.nPlayers())  # Populates the playerList and nPlayers in game object
        game.setGuesses()                 # Sets nGuesses

        # this creates a list of player board instances
        wom.player_board = [Board(each_player, game.n_guesses) for each_player in game.player_list]

        # gets each player to set a code for the next
        game.setCodes()

        # set play_order and begin guessing.
        game.roundRobin()

        print("\nThe game is now finished.")

        for each_player in wom.player_board:
            if each_player.player_name in wom.humans:
                name = each_player.player_name
                index = wom.searchRegPlayers(name)
                wom.reg_players[index].updateScore()

    def quitGame(self):
        print("\nThank you for playing the World of Mastermind!")
        wom.quit_game = True

    def registerPlayer(self):
        new_player_name = input("What is the name of the new user?\n> ")

        if new_player_name not in wom.reg_players:
            # create instance of new player and their name.
            new_player = Players()
            new_player.setName(new_player_name)
            # add them to both the registered players (the list that holds their player instance)
            # and add them to a list of names that the registered players have. To identify against CPU
            wom.reg_players.append(new_player)
            wom.humans.append(new_player.name)

            print("Welcome, " + new_player.getName() + '!')
        else:
            print("Sorry, the name is already taken.")

    def showScoreBoard(self):
        print("=====================================")
        print("Name             Score Games Average")
        print("=====================================")

        for each_player in wom.reg_players:
            try:
                game_ave = each_player.score / each_player.games
            except:
                game_ave = 0.0

            txt = "{:<21}{}{:>6}{:>8}"
            print(txt.format(each_player.name, each_player.score, each_player.games, game_ave))
        print("=====================================")

    def searchRegPlayers(self, name):

        index = 0
        for players in wom.reg_players:
            if players.name == name:
                return index
            else:
                index += 1


class Players:

    def __init__(self):
        self.score = 0
        self.games = 0
        self.name = ''

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def updateScore(self, total_score):
        self.score = self.score + total_score

    def updateGames(self):
        self.games += 1


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
                if player_name not in wom.humans and player_name not in wom.cpu_players:
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

    def setCodes(self):

        # Setting the code for each other
        index = 0
        for each_player in self.player_list:
            if index < len(self.player_list) - 1:
                print('\n* ', each_player, "'s turn to set the code for ", wom.player_board[index + 1].player_name,
                      " to break.", sep='')

                # index + 1 is next player. i.e. Player at index 0 sets for index 1, and so on.
                wom.player_board[index + 1].set_code = wom.player_board[index].setCode()
                print("The code is now set for", wom.player_board[index + 1].player_name, "to break.")

            elif index == len(self.player_list) - 1:
                print('\n* ', each_player, "'s turn to set the code for ", wom.player_board[0].player_name,
                      " to break.", sep='')

                # when index is same as len(), it's the last player, who needs to set code for index 0.
                wom.player_board[0].set_code = wom.player_board[index].setCode()
                print("The code is now set for", wom.player_board[0].player_name, "to break.")

            index += 1

    def roundRobin(self):

        all_complete = False
        while not all_complete:

            play_order = []

            for each_board in wom.player_board:
                if not each_board.correct_guess:
                    if each_board.attempts_left > 0:
                        play_order.append(each_board)

            if len(play_order) == 0:
                all_complete = True

            for each_board in play_order:

                print('\n* ', each_board.player_name, "'s turn to guess the code.", sep='')
                print("Previous attempts:", each_board.attempts_taken)
                # Feedback has to go between attempts taken and attempts left
                # But it doesn't display if there are 0 attempts thus far.
                if each_board.attempts_taken > 0:
                    each_board.giveFeedback()
                print("Attempts left:", each_board.attempts_left)

                # Prompts owner of each board to guess the code
                each_board.current_guess = each_board.setCode()
                # Increment attempts taken and left
                each_board.attempts_taken += 1
                each_board.attempts_left -= 1

                if each_board.testGuess():
                    print(each_board.player_name, "broke the code in", each_board.attempts_taken, "attempts!")
                    each_board.correct_guess = True
                else:
                    print("Feedback: ", end='')
                    print(each_board.feedback)

    def tallyScore(self):

        index = 0

        for each_player in wom.player_board:

            if each_player.player_name in wom.humans:

                name = each_player.player_name
                score_break = each_player.attempts_left

                try:
                    score_set = wom.player_board[index + 1].attempts_taken
                except:
                    score_set = wom.player_board[0].attempts_taken

                total_score = score_break + score_set
                print(name , "receives", score_break, "+",
                      score_set, "=", total_score)

                player_index = wom.searchRegPlayers(name)
                print(player_index)
                print(wom.reg_players[0].score)
                wom.reg_players[player_index].updateScore(total_score)
                print(wom.reg_players[0].score)
                index += 1

        return total_score


class Board:

    def __init__(self, player_name, n_guess):
        self.attempts_taken = 0
        self.attempts_left = n_guess
        self.set_code = ''
        self.current_guess = ''
        self.player_name = player_name
        self.guess_log = []
        self.feedback_log = []
        self.feedback = ''
        self.correct_guess = False

    def setCode(self):

        user_set_code = Code()
        if self.player_name in wom.cpu_players:
            return user_set_code.cpuCode()
        else:
            return user_set_code.setInputCode()

    def testGuess(self):

        # Initial check to bypasss computations in case guess = correct
        if self.current_guess == self.set_code:
            self.correct_guess = True
            return True
        else:
            self.correct_guess = False
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
            self.guess_log.append(self.current_guess)
            return False

    def giveFeedback(self):
        feedback_index = 0

        print("==============")
        print("Code Feedback")
        print("==============")
        for each_score in self.guess_log:
            print(str(each_score), end=' ')
            print(str(self.feedback_log[feedback_index]))
            feedback_index += 1
        print("==============")


class Code:

    def __init__(self):
        self.input_code = ''
        self.allowable_colours = ['R', 'G', 'B', 'Y', 'W', 'K']

    def setInputCode(self):

        while len(self.input_code) != 4:
            self.input_code = input('Please enter the code:\n> ').upper()
            if len(self.input_code) != 4:
                print("Invalid code.")
                print("It must be exactly four characters, each can be R, G, B, Y, W, or K. ")
                self.input_code = 'ERRORFOUND'
            else:
                error_present = False
                for marble in self.input_code:
                    if marble not in self.allowable_colours:
                        error_present = True
                if error_present:
                    print("Invalid code.")
                    print("It must be exactly four characters, each can be R, G, B, Y, W, or K. ")
                    self.input_code = 'ERRORFOUND'
        return self.input_code

    def cpuCode(self):
        for length in range(0,4):
            self.input_code = self.input_code + self.allowable_colours[random.randint(0,5)]

        return self.input_code


wom = WorldOfMastermind()
wom.run()

