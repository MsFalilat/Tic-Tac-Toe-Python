from copy import copy

def printBoard(board):
    print('  |   |')
    print(board['7'] + ' | ' + board['8'] + ' |' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' |' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' |' + board['3'])
    print('  |   |')
    
print("Welcome to Tic Tac Toe!\n")

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

printBoard(board)
print()

print("Player 1 will go first.\n")
turn = input("Player 1: Do you want to be X or O? ")
orig_turn = copy(turn.upper())
turns = 1

while turns < 10:
    pos = input("Chose your next position: (1-9) ")
    board[pos] = turn.upper()
    printBoard(board)
    if turn.upper() == "X":
        turn = "O"
    else:
        turn = "X"
    turns += 1
    
    if (((board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or 
         (board['4'] == "X" and board['5'] == "X" and board['6'] == "X") or 
         (board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or
         (board['7'] == "X" and board['4'] == "X" and board['1'] == "X") or 
         (board['8'] == "X" and board['5'] == "X" and board['2'] == "X") or
         (board['9'] == "X" and board['6'] == "X" and board['3'] == "X") or 
         (board['7'] == "X" and board['5'] == "X" and board['3'] == "X") or 
         (board['9'] == "X" and board['5'] == "X" and board['1'] == "X")) and orig_turn == "X"):
        print(f"Player 1 wins")
        break
    elif (((board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or 
           (board['4'] == "O" and board['5'] == "O" and board['6'] == "O") or 
           (board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or 
           (board['7'] == "O" and board['4'] == "O" and board['1'] == "O") or
           (board['8'] == "O" and board['5'] == "O" and board['2'] == "O") or 
           (board['9'] == "O" and board['6'] == "O" and board['3'] == "O") or 
           (board['7'] == "O" and board['5'] == "O" and board['3'] == "O") or 
           (board['9'] == "O" and board['5'] == "O" and board['1'] == "O")) and orig_turn == "O"):
        print(f"Player 1 wins")
        break
    elif (((board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or 
           (board['4'] == "X" and board['5'] == "X" and board['6'] == "X") or 
           (board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or 
           (board['7'] == "X" and board['4'] == "X" and board['1'] == "X") or 
           (board['8'] == "X" and board['5'] == "X" and board['2'] == "X") or 
           (board['9'] == "X" and board['6'] == "X" and board['3'] == "X") or 
           (board['7'] == "X" and board['5'] == "X" and board['3'] == "X") or 
           (board['9'] == "X" and board['5'] == "X" and board['1'] == "X")) and orig_turn != "X"):
        print(f"Player 2 wins")
        break
    elif (((board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or 
           (board['4'] == "O" and board['5'] == "O" and board['6'] == "O") or 
           (board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or 
           (board['7'] == "O" and board['4'] == "O" and board['1'] == "O") or 
           (board['8'] == "O" and board['5'] == "O" and board['2'] == "O") or 
           (board['9'] == "O" and board['6'] == "O" and board['3'] == "O") or 
           (board['7'] == "O" and board['5'] == "O" and board['3'] == "O") or 
           (board['9'] == "O" and board['5'] == "O" and board['1'] == "O")) and orig_turn != "O"):
        print(f"Player 2 wins")
        break
    else:
        continue
