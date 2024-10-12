from random import randint
from pprint import pprint

SCORES = {"computer" : 0, "player" : 0}

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
        self.player_guesses = []
        self.computer_guesses = []
        self.ships = []


    def print(self):
        for num in range(0, self.size):
            print(num, end=" ")
        print()

        for row in self.board:
            print(" ".join(row))

    # This method is switched up, due to making the 'X' appear on the opposed board
    def guess(self, x, y):
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return True
        else:
            return False


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
    

    if board.type == "player":
        # list1 = [(x, y)]
        player_list = board.player_guesses
        # print(list1)
        # new_guess = set(list1)
        # old_guesses = set(list2)
        # print(new_guess)
        # print(old_guesses)
        try:
            if x < 0 or x >= board.size or y < 0 or y >= board.size:
                raise ValueError(
                    f"Values must be between 0 and {board.size - 1}"
                )
            elif (x, y) in player_list:
                raise ValueError(
                    f"You can't guess the same coordinates twice {player_list}"
                )
            else:
                player_list.append((x, y))
                return True
        except ValueError as e:
            print(f"{e}, please try again.\n")
            return False
        
    # else:
    #     if board.board[x][y] != "." or board.board[x][y] != "@":
    #         return False


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
    
    if board.type == "player":
        while True:
            while True:
                try:
                    x = int(input("Guess a row: \n"))   
                    y = int(input("Guess a column: \n"))
                    break
                except ValueError:
                    print("You must enter a number!")
         
            if valid_coordinates(x, y, board):
                print(f"{board.name} guessed: {x, y}")
                break
        
    else:
        size = board.size
        x = random_point(size)
        y = random_point(size)
        # if valid_coordinates(x, y, board):
        #     print(f"{board.name} guessed: {x, y}")

    return x, y
    


def play_game(computer_board, player_board):
    """

    """
    while True:
        print(f"{computer_board.name}'s Board:")
        computer_board.print()
        print("-" * player_board.size * 2)
        print(f"{player_board.name}'s Board:")
        player_board.print()

        player_awnser = make_guess(player_board)
        player_result_win = computer_board.guess(*player_awnser)

        if player_result_win:
            print(f"{player_board.name} got a hit!!")
        else:
            print(f"{player_board.name} missed this time.")

        computer_awnser = make_guess(computer_board)
        computer_result_win = player_board.guess(*computer_awnser)

        if computer_result_win:
            print(f"{computer_board.name} got a hit!!")
        else:
            print(f"{computer_board.name} missed this time.")
    

def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    scores and initialises the board
    """

    size = 10
    num_ships = 4
    SCORES["computer"] = 0
    SCORES["player"] = 0
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
