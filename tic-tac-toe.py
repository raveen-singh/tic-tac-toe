# tic-tac-toe
from IPython.display import clear_output
import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]


def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def order_of_play():
    players = ["Player 1", "Player 2"]
    global rand
    rand = random.choice(players)
    print("The player going first is", rand)
    global opp_rand
    if rand == "Player 1":
        opp_rand = "Player 2"
    else:
        opp_rand = "Player 1"

def x_or_o():
    print(rand,"do you want to be X or O?")
    marker = input()
    if marker == "X" or "x":
        print(rand, "is now X")
        print(opp_rand, "is now O")


def player_one(row, col):
    print(rand, "What is your first move?")
    print(col)
    print(row)
    row = (input("What row do you want to go in?"))
    col = (input("What col do you want to go?"))



def player_two(row1, col1):
    print(opp_rand, "What is your move")
    print(col1)
    print(row1)


#row1 = (input("What row do you want to go in?"))
#col1 = (input("What col do you want to go?"))

print_board()
order_of_play()
x_or_o()
player_one(row, col)
