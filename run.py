from random import randint
from pprint import pprint

scores = {"computer" : 0, "player" : 0}

class Board:
    """
    Main board class. Sets board size, the number of ships,
    the players's name and the board type (player board or computer)
    Has methods for add ships and guesses, and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [['.' for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for num in range(0, self.size):
            print(num, end=" ")
        print()

        
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
    
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add anymore ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"
    
def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """

    return randint(0, size -1)


def valid_coordinates(x, y, board):
    """
    
    """
    # try:


def populate_board(board):
    """

    """
    size = board.size
    x = random_point(size)
    y = random_point(size)
    board.add_ship(x, y)


def make_guess(board):
    """

    """

def play_game(computer_board, player_board):
    """

    """
    print(f"{computer_board.name}'s Board:")
    computer_board.print()
    print("-" * player_board.size * 2)
    print(f"{player_board.name}'s Board:")
    player_board.print()

def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    scores and initialises the board
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(" Welcome to ULTIMATE BATTLESHIPS!!")
    print(f" Board size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(computer_board)
        populate_board(player_board)
    
    play_game(computer_board, player_board)

new_game()
