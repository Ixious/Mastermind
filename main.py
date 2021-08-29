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
    """
    This is a class for key operations within the Mastermind gameplay
        such as the main run() method which calls all further methods and instantiates other
        objects, and other methods such as playGame() quitGame() etc.

    Attributes:
        cpu_players (list): List containing the str names of CPU operated players.
        humans      (list): List which will house the names of registered human players.
        reg_players (list): List containing Player() objects [which contains score, games, name].
        player_board(list): List containing Board() objects [a new board for each player in the round].
        quit_game   (bool): Used to quit program on user command.
    """

    def __init__(self):
        """
        Constructor for WorldOfMastermind
        :parameter self
        :returns nil
        """
        self.cpu_players = ['HAL9000','VIKI']
        self.humans = []
        self.reg_players = []
        self.player_board = []
        self.quit_game = False

    def run(self):
        """
        This method is the only method to be called from outside wom.run()
            it prints intro text, and calls wom.options()

        :parameter self
        :returns nil
        """

        # Intro text, only to be displayed on initial opening of game.
        print("Welcome to the World of Mastermind!")
        print("Developed by Mason Manuel")
        print("COMP 1048 UO Object-Oriented Programming")

        # Initiates options screen, this is a while loop that only progresses
        # when wom.options returns bool True for play_game. (user selects play)
        wom.options()

    def options(self):
        """
        The function that acts as a menu for the user. wom.options() takes user input and calls
            the method associated with that input i.e wom.registerPlayer() == 'r', after the method call,
            the user selection is reverted to blank to restart the loop, allowing players to make a further
            selection

        :parameter self
        :returns nil
        """

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
        """
        This is the class method which allows for gameplay. Calling this method creates ONE
            instance of Game() and then calls Game() methods to populate it's own attributes
            n_players, player_list, and n_guesses. These attributes are the 'rules' of the round.
        It creates a list containing a Board() object for each_player contained in the player_list
            it then calls methods which set the codes for each board, and then allow users to attempt to break
            their code.

        :parameter self
        :return: nil
        """

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

        game.tallyScore()

    def quitGame(self):
        """
        Called when user_selection in wom.options() == 'q'
        This method prints the end text and sets the wom.quit_game attribute to True, signalling the end
            of the wom.options() loop, and ending program execution.

        :parameter self
        :return: nil
        """
        print("\nThank you for playing the World of Mastermind!")
        wom.quit_game = True

    def registerPlayer(self):
        """
        Called when wom.options user_selection == 'r'
        This method creates a new instance of Player() by taking input from the user for the
            new_player_name. Checks this name against the wom.humans list to avoid double-ups
            and then creates Player() object, and adds object to wom.reg_players list
        Also displays some text to greet player or to show error.

        :return: nil
        """
        new_player_name = input("What is the name of the new user?\n> ")

        if new_player_name not in wom.humans:
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
        """
        Method displays scoreboard and calculates the players average score.
        Tries to divide each_player.score by each_player.games, and handles exceptions of
        ZeroDivisionError by setting game_ave = 0.0

        :returns nil
        """
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
        """
        Clever method searches the wom.reg_players list of Player() objects by checking each objects
            name attribute. if the player.name = name passed in as an argument, then the Player object
            that is being searched for is at the index specified i.e. wom.reg_players[index]

        This is used so that other attributes for Player objects can be updated, such as score/games.
        :param name:
        :return: index
        """

        index = 0
        for players in wom.reg_players:
            if players.name == name:
                return index
            else:
                index += 1


class Players:
    """
    This is the Players class. It has functions to update and get attributes related to a Player object

    Attributes:
         score (int): a container for a Player objects running score, this is updated after rounds
         games (int): holds how many games object has participated in, incremented each round
         name  (str): is the name of the player which the Player object was created for
    """

    def __init__(self):
        """
        Constructor for Player class
        :parameter self
        :returns nil
        """
        self.score = 0
        self.games = 0
        self.name = ''

    def setName(self, name):
        """
        Method for setting Player.name to specified string gets the name parameter
        from wom.registerPlayer()

        :param name:
        :return: none
        """
        self.name = name

    def getName(self):
        """
        This function can be called to request the name of a Player object, when called returns
        player.name as str

        :return: name
        """
        return self.name

    def updateScore(self, total_score):
        """
        This method updates the Player attribute 'player.score' through addition of 'total_score'
        to the existing value held within the player.score variable. this is called at the end of a
        wom.playGame() round.

        :param total_score:
        :return:
        """
        self.score = self.score + total_score

    def updateGames(self):
        """
        This method increments the attribute 'player.games' by an integer of 1, this is called at the
        end of a wom.playGame() round

        :return:
        """
        self.games += 1


class Game:
    """
    When wom.playGame() is called, it creates an instance of a Game object. The Game class
    has attributes which set the 'rules' of the game: number of players (n_players), number of allowed
    guesses (n_guesses), and a list of the current players (player_list). The class has functions to set
    the attributes of the object, as well as methods which are used for the game to operate, such as
    setting the code to break, or creating a play order for players to play in a round robin style.

    Attributes:
        n_players   (int)
        n_guesses   (int)
        player_list (list)
    """

    def __init__(self):
        """
        Constructor for Game class
        """
        self.n_players = 0
        self.n_guesses = 0
        self.player_list = []

    def nPlayers(self):
        """
        nPlayers(self) first prints the beginning text, and then checks to see that the n_players has not
        yet been set. It takes user input to set the n_players attribute, it then validates the user input
        by checking if it is numeric, and then if it is within the acceptable range of 2-4.
        :return:
        """
        print("Let’s play the game of Mastermind!")

        while self.n_players not in range(2,5):
            self.n_players = input("How many players (2-4)?\n> ")

            if not self.n_players.isnumeric():
                print("Number of players must be between 2-4")
            else:
                self.n_players = int(self.n_players)

                if self.n_players not in range(2,5):
                    print("Number of players must be between 2-4")

        return self.n_players

    def playerList(self, n_players):
        """
        This method sets allows the user to select which players are going to play the round of
            mastermind. it uses n_players to determine the correct amount of times to ask for user input
            and checks the user input against player names found in the wom.humans and wom.cpu_players list
            if they are not in those lists, they are not yet registered and cannot play a round
        :param n_players:
        :return:
        """

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
        """
        setGuesses(self) takes user input to set game.n_guesses as an integer between 5 and 10.
            it checks the input to ensure it is both numeric and that the integer falls between the
            correct range of 5-10 inclusive.
        :return:
        """

        while self.n_guesses not in range(5,11):

            self.n_guesses = input("How many attempts will be allowed for each player (5-10)?\n> ")
            if not self.n_guesses.isnumeric():
                print("Number must be between 5-10")
            else:
                self.n_guesses = int(self.n_guesses)

                if self.n_guesses not in range(5, 11):
                    print("Number must be between 5-10")

    def setCodes(self):
        """
        This method will ask for input from a player to set the code for their opponent. #1 sets for #2,
            #2 sets for #3, #3 sets for #4, and #4 sets for #1. It achieves this by going through each_player
            in self.player_list (set by game.PlayerList()) and requesting input each time.
        This method tests if the current each_player is the last one by comparing it length of the player_list
            if it is the last player in the list, it sets the code for player_list at index [0]

        This method makes a call to Board.setCode().
        :return:
        """

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
        """
        roundRobin(self) is a method which loops until the boolean 'all_complete' is altered to True.
        while the loop is active, it goes through the board objects contained in the wom.player_board list
        checks each boards attribute 'correct_guess' and also 'attempts_left'. If the board object has
        False correct_guess and has > 0 attempts remaining, then it is added to the play_order list.

        This allows for the game to be played in a round-robin style where guessing is taken in turns. If one
        player finishes, they won't be added to the play_order and play will resume only for those contained
        in the list.

        If no boards in wom.player_board pass both checks, the list will be empty, thus the len(play_order)
        would be 0, this sets all_complete to True and ends the while loop.

        This function also calls to method: Board.giveFeedback()

        Attributes:
            all_complete (bool)
            play_order (list)
        :return:
        """
        all_complete = False        # Used to break out of the while loop when changed to True.
        while not all_complete:

            play_order = []

            for each_board in wom.player_board:
                if not each_board.correct_guess:
                    if each_board.attempts_left > 0:
                        play_order.append(each_board)

            # If no boards in wom.player_board pass both checks, the list is empty, and all games
            # are complete
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
        """
        tallyScore(self) is called by wom.playGame() after game.roundRobin(). It allows for
            Player object scores to be updated through utilising the board attributes: attempts_taken,
            and attempts_left, and by calling the wom.searchRegPlayers() method to find the correct index
            to update player scores, also updates player.game while it has the correct player_index
            handy.

        :return:
        """

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

                wom.reg_players[player_index].updateScore(total_score)
                wom.reg_players[player_index].updateGames()

            index += 1


class Board:
    """
    Board class objects are created for each player, so there are between 2-4 boards created.
    each board holds attributes that have been dictated by the game 'rules' such as the attempts_left.
    as well as attributes pertaining to this board only, such as guess_log, feedback_log etc.

    Attributes:
        attempts_taken (int): initializes at 0
        attempts_left (int): from n_guess argument
        set_code (str): set by board.setCode
        current_guess (str) set by board.setCode each turn of roundRobin
        player_name (str) from player_name argument
        guess_log (list): list of all guess attempts
        feedback_log (list): list of all feedback
        feedback (str): current feedback, resets each turn of roundRobin
        correct_guess (bool): used to signify that this board is finished to roundRobin
    """

    def __init__(self, player_name, n_guess):
        """
        Constructor for Board class. takes 2 parameters of player_name and n_guess

        :param player_name:
        :param n_guess:
        """
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

        """
        setCode is a method which creates an instance of Code(). It then runs a check to see if
        the player is a CPU (HAL9000, VIKI) or a human. It returns the result of either
        user_set_code.cpuCode() - which is a randomly generated code for CPU players OR
        user_set_code.setInputCode() - which asks the human user for keyboard input.

        :return: result of either Code.cpuCode() or Code.setInputCode()
        """

        user_set_code = Code()
        if self.player_name in wom.cpu_players:
            return user_set_code.cpuCode()
        else:
            return user_set_code.setInputCode()

    def testGuess(self):

        """
        This method compares the boards current_guess and set_code attributes. If these attributes
            are equal then the attribute correct_guess will be modified to True.
            if they are not equal it creates new_list: a list that holds each individual str character
            from Board.set_code. It then compares each str char/"marble" against the items in new_list.

        First it checks for correct colour and index, and will add a 'K' to the Board.feedback, it will then
            delete that piece of data from new_list so that duplicate feedback is not given. Once this is
            done, any marbles that gave feedback K have been removed, then the marbles are compared against
            the remaining items in new_list to give the 'W' feedback to signify that the colour is in there,
            just not in the correct index.

        :return: bool
        """

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
        """
        This method prints specified lines of text as well as the feedback_log list as a string.
        and the guess_log list as a string, formatted as per specifications.
        :return:
        """
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

