import random

print("Welcome to the Tic-Tac-Toe game!")
print("Type the corresponding number to your desired position when it is your turn.")

template_board = {i+1: i+1 for i in range(9)}
game_board = {i+1: " " for i in range(9)}
available_moves = [i+1 for i in range(9)]

def print_board(board):
    print()
    print(str(board[1]) + " | " + str(board[2]) + " | " + str(board[3]))
    print("--+---+--")
    print(str(board[4]) + " | " + str(board[5]) + " | " + str(board[6]))
    print("--+---+--")
    print(str(board[7]) + " | " + str(board[8]) + " | " + str(board[9]))
    print()

def check_win():
    if game_board[1] == game_board[2] == game_board[3] != " ":
        return True
    if game_board[4] == game_board[5] == game_board[6] != " ":
        return True
    if game_board[7] == game_board[8] == game_board[9] != " ":
        return True
    if game_board[1] == game_board[4] == game_board[7] != " ":
        return True
    if game_board[2] == game_board[5] == game_board[8] != " ":
        return True
    if game_board[3] == game_board[6] == game_board[9] != " ":
        return True
    if game_board[1] == game_board[5] == game_board[9] != " ":
        return True
    if game_board[3] == game_board[5] == game_board[7] != " ":
        return True


print_board(template_board)

while True:
    key = input("Press ENTER to start the game: ")
    if key == "":
        break
    else:
        print("That was not the ENTER key.")

while True:
    game_mode = input("Press 1 if you want to play with another person or 2 if you want to play against an A1. ")
    if game_mode in ["1", "2"]:
        break
    else:
        print("That was not a 1 or 2. Retry.")

def play_game():      
    if int(game_mode) == 1:
        for i in range(9):
            if i % 2 == 0:
                while True:
                    move_string = input("Player 1's turn: Enter a position. ")
                    if move_string in "123456789" and game_board[int(move_string)] == " ":
                        game_board[int(move_string)] = "X"
                        print_board(game_board)
                        if check_win() == True:
                            print("Player 1 won!")
                            return
                        break
                    else:
                        print("That position is already taken. Please enter an open one. ")
            else:
                while True:
                    move_string = input("Player 2's turn: Enter a position. ")
                    if move_string in "123456789" and game_board[int(move_string)] == " ":
                        game_board[int(move_string)] = "O"
                        print_board(game_board)
                        if check_win() == True:
                            print("Player 2 won!")
                            return
                        break
                    else:
                        print("That position is already taken. Please enter an open one. ")
        print("It's a tie!")
    elif int(game_mode) == 2:
        for i in range(9):
            if i % 2 == 0:
                while True:
                    move_string = input("Your turn: Enter a position. ")
                    if move_string in "123456789" and game_board[int(move_string)] == " ":
                        available_moves.remove(int(move_string))
                        game_board[int(move_string)] = "X"
                        print_board(game_board)
                        if check_win() == True:
                            print("You won!")
                            return
                        break
                    else:
                        print("That position is already taken. Please enter an open one. ")
            else:
                move_integer = random.choice(available_moves)
                available_moves.remove(move_integer)
                game_board[move_integer] = "O"
                print_board(game_board)
                if check_win() == True:
                    print("The AI won!")
                    return
                    
        print("It's a tie!")

play_game()
print("Thanks for playing!")