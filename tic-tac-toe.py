# tic-tac-toe
import random

board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
again = "Y"

def names():
    print("Player 1, what is your name?")
    global name1
    name1 = input()
    print("Player 2, what is your name?")
    global name2
    name2 = input()

def print_board():
    print(*board[0],'')
    print(*board[1],'')
    print(*board[2],'')

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
    while True:
        marker = input(str()).upper()
        if marker != "X" or marker != "O":
            print('Invalid input. Please enter X or O')
            continue
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
    while True:
        print(rand, "what row do you want to go in?")
        row = int(input())
        print(rand, "what col do you want to go?")
        col = int(input())
        if row > 3:
            print("Number of rows is out a range. Please re-enter your moves")
            continue
        if col > 3:
            print("Number of cols is out a range. Please re-enter your moves")
            continue
        if board[row - 1][col -1] == "X" or board[row - 1][col -1] == "O":
            print("Uh-Oh, there is already something there. Please re-enter your moves")
            continue
        else:
            break
    board[row - 1][col -1] = marker

def player_two():
    while True:
        print(opp_rand, "what row do you want to go in?")
        row = int(input())
        print(opp_rand, "what col do you want to go?")
        col = int(input())
        if row > 3:
            print("Number of rows is out a range. Please re-enter your moves")
            continue
        if col > 3:
            print("Number of cols is out a range. Please re-enter your moves")
            continue
        if board[row - 1][col -1] == "X" or board[row - 1][col -1] == "O":
            print("Uh-Oh, there is already something there. Please re-enter your moves")
            continue
        else:
            break
    board[row - 1][col -1] = opp_marker

def full_board():
    global again
    new_list = ""
    for sublist in board:
        for n in sublist:
            new_list += str(n)
    if '.' in new_list:
        pass
    else:
        while True:
            print("Tie Game. Would you like to play again? Enter Y or N")
            again = input().upper()
            if again != "Y" or again != "N":
               print("Invalid input. Please enter Y or N")
               continue
            if again == "Y":
               clear_board()
            if again == "N":
                print("See you later")
                pass

def won_game_x():
    global again
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" \
        or board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" \
        or board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" \
        or board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" \
        or board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" \
        or board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" \
        or board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X" \
        or board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":

        print("X has Won!! Would you like to play again? Please enter Y or N")
        while True:
            again = input().upper()
            if again != "Y" or again != "N":
                print("Invalid input. Please enter Y or N")
                continue
            if again == "Y":
                clear_board()
            if again == "N":
                print("See you later!")

def won_game_o():
    global again
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" \
        or board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" \
        or board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" \
        or board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" \
        or board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" \
        or board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" \
        or board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O" \
        or board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":

        print("O has Won!! Would you like to play again? Please enter Y or N")
        while True:
            again = input().upper()
            if again != "Y" or again != "N":
                print("Invalid input. Please enter Y or N")
                continue
            if again == "Y":
                clear_board()
            if again == "N":
                print("See you later!")

def clear_board():
    global board
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


def play_game():
    names()
    order_of_play()
    x_or_o()

    while True:

        print_board()
        player_one()
        won_game_x()
        global again
        if again == "N":
            break
        print(again)
        won_game_o()
        if again == "N":
            break
        full_board()
        if again == "N":
            break
        print_board()
        player_two()
        won_game_x()
        if again == "N":
            break
        won_game_o()
        if again == "N":
            break
        full_board()
        if again == "N":
            break

play_game()

