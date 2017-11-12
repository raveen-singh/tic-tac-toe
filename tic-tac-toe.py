# tic-tac-toe
from IPython.display import clear_output
import random

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
win = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]

def names():
    print("What is your name?")
    global name1
    name1 = input()
    print("What is your name?")
    global name2
    name2 = input()

def print_board():
    print(board[0])
    print(board[1])
    print(board[2])

def order_of_play():
    players = [name1, name2]
    global rand
    rand = random.choice(players)
    print("The player going first is", rand)
    global opp_rand
    if rand == name1:
        opp_rand = name2
    else:
        opp_rand = name1

def x_or_o():
    print(rand,"do you want to be X or O?")
    global marker
    marker = input(str())
    print(marker)
    if marker == "X" or marker == "x":
        global opp_marker
        opp_marker = "O"
        print(rand, "is X")
        print(opp_rand, "is O")
    elif marker == "O" or marker =="o":
        opp_marker = "X"
        print(rand, "is O")
        print(opp_rand, "is X")


def player_one():
    print(rand, "what row do you want to go in?")
    row = int(input())
    print(rand, "what col do you want to go?")
    col = int(input())
    board[row - 1][col -1] = marker

def player_two():
    print(opp_rand, "what row do you want to go in?")
    row = int(input())
    print(opp_rand, "what col do you want to go?")
    col = int(input())
    board[row - 1][col -1] = opp_marker





names()
order_of_play()
x_or_o()
print_board()
player_one()
print_board()
player_two()
print_board()
