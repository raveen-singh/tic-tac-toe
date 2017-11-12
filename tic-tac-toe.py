# tic-tac-toe
from IPython.display import clear_output
import random

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
win = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]

def names():
    print("Player 1, what is your name?")
    global name1
    name1 = input()
    print("Player 2, what is your name?")
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
    marker = input(str()).upper()
    print(marker)
    if marker == "X":
        global opp_marker
        opp_marker = "O"
        print(rand, "is X")
        print(opp_rand, "is O")
    elif marker == "O":
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

def full_board():
    for i in range(len(board)):
            if i == "X" or i == "O":
                print("Tie Game. Would you like to play again? Enter Y or N")
                again = input().upper()
                if again == "Y":
                    continue
                else:
                    break
def won_game_x():
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" \
        or board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" \
        or board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" \
        or board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" \
        or board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" \
        or board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" \
        or board[0][1] == "X" and board[1][1] == "X" and board[2][0] == "X" \
        or board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":

        print("X has Won!! Would you like to play again? Please enter Y or N")
        again = input().upper()
        if input == "Y":
            print("ok")
        elif input == "N":
            print("See you later!")

def won_game_o():
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" \
        or board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" \
        or board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" \
        or board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" \
        or board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" \
        or board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" \
        or board[0][1] == "O" and board[1][1] == "O" and board[2][0] == "O" \
        or board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":

        print("O has Won!! Would you like to play again? Please enter Y or N")
        again = input().upper()
        if input == "Y":
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print("ok")
        elif input == "N":
            print("See you later!")
names()
order_of_play()
x_or_o()
while True:

    print_board()
    player_one()
    won_game_x()
    won_game_o()
    full_board()
    print_board()
    player_two()
    won_game_x()
    won_game_o()
    full_board()
