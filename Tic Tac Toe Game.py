import os

def initialize_board():
    board  = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
    return board

def display_board(board):
    for idx,row in enumerate(board):
        print('|'.join(row))
        # Only print the separator for the first two rows
        if idx <len(board) - 1:
            print("-----")

def get_player_move():
    row = int(input("Enter the row(0,1,2) : "))
    column = int(input("Enter the Column(0,1,2) : "))
    return row,column

def move_valid(board , move):
    row , col = move
    if board[row][col] == " ":
        return True
    return False

def make_move(board , current_player , move):
    row , col = move
    board[row][col] = current_player

def check_winner(board , current_player):
    for i in range(3):
        if all(board[i][j] == current_player for j in range(3)) or \
        all(board[j][i] == current_player for j in range(3)) or \
        all(board[i][i] == current_player for i in range(3)) or \
        all(board[i][2-i] == current_player for i in range(3)):
            return True
    return False

def check_board_full(board, move):
    row , col =move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
    
def play_tic_tac_toe():
    board = initialize_board()
    current_player = 'X'

    while True:
        os.system('cls')
        display_board(board)
        print(f"Its Player {current_player}'s Turn.")
        move = get_player_move()

        #Check if the players move is valid or not
        if move_valid(board , move):
            make_move(board , current_player , move)

            #Check if player wins the game
            if check_winner(board , current_player):
                print(f"Player {current_player} Wins The Game!")
                break

            #Check if the board is full
            elif check_board_full(board,move):
                print("It's a Draw")
                break
            
            else:
                #Change players turn
                current_player = '0' if current_player == 'X' else 'X'
    
        else:
            #Tell user to make a valid move
            print("Invalid Move. Try Again")

#run the game
play_tic_tac_toe()

