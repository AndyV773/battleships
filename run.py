from random import randint
# This channel helped with colorama https://youtu.be/u51Zjlnui4Y?si=8G1BQBbluJfsmED7
import colorama
from colorama import Fore, Back, Style
# Resets colors after each initiation
colorama.init(autoreset=True)

# Global colors/colours variabls
BRIGHT_BLUE = "\033[34;1m"
BRIGHT_CYAN = "\033[36;1m"
BRIGHT_RED = "\033[31;1m"
BRIGHT_YELLOW = "\033[33;1m"
BRIGHT_GREEN = "\033[32;1m"
BRIGHT_MAGENTA = "\033[35;1m"

COLORS = [BRIGHT_YELLOW, BRIGHT_MAGENTA, BRIGHT_BLUE, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_RED]
COLOR_INDEX = 0

# Global variables
SCORES = {"computer" : 0, "player" : 0}
# Helper variable to break out of play game while loop
PLAY_GAME = True
LOOP_COUNTER = 1

# Some of the code in the Board class come from code insitute https://p3-battleships.herokuapp.com/
class Board:
    """
    Main board class. Sets board size, the number of ships,
    the players's name and the board type (player board or computer)
    Has methods for add ships and guesses, and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [[f"{BRIGHT_CYAN}." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.player_guesses = []
        self.computer_guesses = []
        self.ships = []


    def print(self):
        """
        
        """

        space = " "
        if self.size < 10:
            print(space, end=" ")
            for num in range(0, self.size):
                print(BRIGHT_GREEN + str(num), end=" ")
            print()
            # Had to do some research, but this helped with some pointers https://python-forum.io/thread-362.html
            for i, row in enumerate(self.board):
                print(BRIGHT_GREEN + str(i), space.join(row))
        else:
            space *= 2
            for num in range(10):
                print(BRIGHT_GREEN + str(num), end=space)
            for num in range(10, self.size):
                print(BRIGHT_GREEN + str(num), end=" ")
            print()
            for i, row in enumerate(self.board):
                print(space.join(row), BRIGHT_GREEN + str(i))


    # This method is switched up, due to making the 'X' appear on the opposed board
    def guess(self, x, y):
        """
        
        """

        self.board[x][y] = f"{BRIGHT_GREEN}X"

        if (x, y) in self.ships:
            self.board[x][y] = f"{BRIGHT_RED}*"
            return True
        else:
            return False


    # code for add ship method from code insitute https://p3-battleships.herokuapp.com/
    def add_ship(self, x, y, type="computer"):
        """
        
        """

        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add anymore ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = f"{BRIGHT_YELLOW}@"


# code for random point function from code insitute https://p3-battleships.herokuapp.com/
def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """

    return randint(0, size -1)


def populate_board(board):
    """

    """
    size = board.size
    x = random_point(size)
    y = random_point(size)
    board.add_ship(x, y)


def adjust_scores(board):
    """
    Adds 1 to player or computers score
    """

    if board.type == "player":
        SCORES["player"] = SCORES["player"] +1
    else:
        SCORES["computer"] = SCORES["computer"] +1


def valid_coordinates(x, y, board):
    """
    Appends the values x and y to the corresponding player's _guesses list.
    Returns True if x and y are within range of the class size 
    and have not been used before (i.e, appended to the _guesses list)
    """
    
    if board.type == "player":
        player_list = board.player_guesses
        if x < 0 or x >= board.size or y < 0 or y >= board.size:
            print(f"{BRIGHT_RED}Values must be between 0 and {board.size - 1}")
        elif (x, y) in player_list:
            print(BRIGHT_RED + "You can't guess the same coordinates twice: ".upper() + BRIGHT_GREEN + str(player_list))
        else:
            player_list.append((x, y))
            return True
        
    else:
        computer_list = board.computer_guesses
        if (x, y) in computer_list:
            return False
        else:
            computer_list.append((x, y))
            return True


def make_guess(board):
    """

    """

    if board.type == "player":
        while True:
            while True:
                try:
                    x = int(input(f"{BRIGHT_BLUE}Guess a row {BRIGHT_GREEN}0 {BRIGHT_BLUE}- {BRIGHT_GREEN}{board.size -1}{BRIGHT_BLUE}:{BRIGHT_GREEN} \n"))   
                    y = int(input(f"{BRIGHT_BLUE}Guess a column {BRIGHT_GREEN}0 {BRIGHT_BLUE}- {BRIGHT_GREEN}{board.size -1}{BRIGHT_BLUE}:{BRIGHT_GREEN} \n"))
                    break
                except ValueError:
                    print(BRIGHT_RED + "You must enter a number!".upper())
         
            if valid_coordinates(x, y, board):
                print(f"{BRIGHT_CYAN}{board.name} {BRIGHT_BLUE}guessed: {BRIGHT_GREEN}{x, y}")
                break
        
    else:
        while True:
            size = board.size
            x = random_point(size)
            y = random_point(size)
            if valid_coordinates(x, y, board):
                print(f"{BRIGHT_CYAN}{board.name} {BRIGHT_BLUE}guessed: {BRIGHT_GREEN}{x, y}")
                break

    return x, y


def win_lose(computer_board, player_board):
    """
    
    """
    if SCORES["player"] == computer_board.num_ships or SCORES["computer"] == player_board.num_ships:
        if SCORES["player"] == computer_board.num_ships and SCORES["computer"] == player_board.num_ships:
            print(BRIGHT_RED + "GAME OVER!!")
            print(BRIGHT_YELLOW + "It was a draw! Better luck next time.")
        elif SCORES["player"] == computer_board.num_ships:
            print(BRIGHT_GREEN + "Well done!! You are the victor!!")
        elif SCORES["computer"] == player_board.num_ships:
            print(BRIGHT_RED + "GAME OVER!!")
            print(BRIGHT_RED + "Bad luck! The computer beat you.")
        return True
    else:
        return False


def play_game(computer_board, player_board):
    """

    """
    print('IN: play_game')
    global PLAY_GAME
    global LOOP_COUNTER
    global COLORS
    global COLOR_INDEX

    while PLAY_GAME == True:
        print('IN: play_game WHILE LOOP')

        print(f"{BRIGHT_CYAN}{computer_board.name}'s {BRIGHT_BLUE}Board:")
        computer_board.print()
        print(BRIGHT_YELLOW + "-" * player_board.size * 3)
        print(f"{BRIGHT_CYAN}{player_board.name}'s {BRIGHT_BLUE}Board:")
        player_board.print()

        player_awnser = make_guess(player_board)
        player_result_win = computer_board.guess(*player_awnser)

        if player_result_win:
            adjust_scores(player_board)
            print(BRIGHT_RED + player_board.name.upper() + " got a Hit!!".upper())
        else:
            print(f"{BRIGHT_YELLOW}{player_board.name} missed this time.")

        computer_awnser = make_guess(computer_board)
        computer_result_win = player_board.guess(*computer_awnser)

        if computer_result_win:
            adjust_scores(computer_board)
            print(BRIGHT_RED + computer_board.name.upper() + " got a Hit!!".upper())
        else:
            print(f"{BRIGHT_YELLOW}{computer_board.name} missed this time.")
        
        print(BRIGHT_YELLOW + "-" * 35)
        print(BRIGHT_BLUE + "After this round the scores are:")
        print(f"{BRIGHT_BLUE}{player_board.name}: {BRIGHT_GREEN + str(SCORES["player"])} {BRIGHT_BLUE}/ {computer_board.name}: {BRIGHT_GREEN + str(SCORES["computer"])}")
        print(BRIGHT_YELLOW + "-" * 35)

        results = win_lose(computer_board, player_board)

        if end_game(results) == True:
            break
        
    if COLOR_INDEX > 5:
        COLOR_INDEX = 0

    print(COLORS[COLOR_INDEX] + f"Shutting Down Battle Station {LOOP_COUNTER}...")
    LOOP_COUNTER += 1
    COLOR_INDEX += 1
    PLAY_GAME = False


def end_game(results):
    """
    
    """

    player_continue = input(BRIGHT_BLUE + "Enter any key to continue or n to quite: \n" + BRIGHT_CYAN)

    if player_continue.lower() == "n":
        print(BRIGHT_RED + "Shutting Down Battle Stations!")
        return True
    elif results == True and player_continue.lower() != "n":
        print(BRIGHT_GREEN + "Initialising New Battle Ships...")
        new_game()
    else:
        print(BRIGHT_GREEN + "Reloading Battle Stations...")
        return False
            


# Some of the code for the new game function come from code insitute https://p3-battleships.herokuapp.com/
def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    scores and initialises the board
    """

    while True:
        try:
            size = int(input(BRIGHT_BLUE + "Please enter size of map 2 - 50: \n" + BRIGHT_GREEN))
            if size < 2 or size > 50:
                raise ValueError
            break
        except ValueError:
            print(BRIGHT_RED + "You must enter a number between 2 and 50!".upper())
            
    while True:
        try:
            max_ships = size / 1.2
            if size <= 3:
                num_ships = 1
            else:
                num_ships = int(input(BRIGHT_BLUE + f"Please enter the number of ships 1 - {int(max_ships)}: \n" + BRIGHT_GREEN))
            if num_ships < 1 or num_ships > max_ships:
                raise ValueError
            break
        except ValueError:
            print(BRIGHT_RED + f"You must enter a number between 1 and {int(max_ships)}!".upper())
    SCORES["computer"] = 0
    SCORES["player"] = 0
    print(BRIGHT_YELLOW + "-" * 35)
    print(BRIGHT_BLUE + " Welcome to ULTIMATE BATTLESHIPS!!")
    print(f" {BRIGHT_BLUE}Board size: {BRIGHT_GREEN}{size}{BRIGHT_BLUE}. Number of ships: {BRIGHT_GREEN}{num_ships}")
    print(f" {BRIGHT_BLUE}Top left corner is row: {BRIGHT_GREEN}0{BRIGHT_BLUE}, col: {BRIGHT_GREEN}0")
    print(BRIGHT_YELLOW + "-" * 35)
    player_name = input(BRIGHT_BLUE + "Please enter your name: \n" + BRIGHT_CYAN)
    print(BRIGHT_YELLOW + "-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(computer_board)
        populate_board(player_board)
    
    play_game(computer_board, player_board)

new_game()
