from copy import copy

#This function prints out the tic-tac-toe board
def printBoard(board):
    print('   |   |')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('---+---+---')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('---+---+---')
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('   |   |')

#This function asks the user if they would like to play again or not
def replay():
    replay = ''

    while True:
        if (replay.upper() == "Y" or replay.upper() == "N" or replay.upper() == "YES" or replay.upper() == "NO"):
            if (replay.upper() == "Y" or replay.upper() == "YES"):
                print('\n'*10)
                ticTacToe()
                replay = ''
                continue
            else:
                print("Till next time!")
                break
        else:
            replay = input("Would you like to play again? (Y or N) ")

	    
def ticTacToe():
    print("Welcome to Tic Tac Toe!\n")

    """
    Dictionary representation of the tic-tac-toe board. The positions on the board
    follow the "numpad" sequence on a keyboard.
    """

    board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

    #print an initial empty tic-tac-toe board
    printBoard(board)
    print()

    print("Player 1 will go first.\n")
    choice = '' #string variable storing each players choice throughout the game

    """
    If Player 1 enters anything besides an "X" or an "O", it will
    keep prompting user for a choice until a valid input is entered.
    """
    while True:
        if (choice.upper() == "X" or choice.upper() == "O"):
            break
        else:
            choice = input("Player 1, Choose X or O: ")
            continue

    orig_choice = copy(choice.upper()) #stores a copy of Player 1's choice of X or O
    turns = 1  #Number of turns starting from turn 1

    """
    There can be a maximum of 9 turns overall in a tic-tac-toe game. So while the
    value of the turns variable is less than 10 (a.k.a 1 to 9), this while loop will
    execute.
    """
    while turns < 10:
        pos = input(f"This turn is for {choice.upper()}. Choose your position (1-9): ") #stores the position player picks to play to

        """
        if the position the player entered is not between 1 and 9, let them know
        and continue prompting to pick a position until a valid input is read
        """
        if pos not in '123456789':
            print("You must enter a value between 1 and 9")
            continue
        else: #if the position is between 1 and 9
            if board[pos] == ' ': #if the position on the board if empty
                board[pos] = choice.upper() #fill that position on the board with the player's choice
            else: #otherwise notify player that the position is filled and prompt them to choose an valid position
                print("That position is already filled. Pick a valid empty position.")
                continue

        printBoard(board) #print the current board with the player's choice filled in

        #if the current player is "X" change it to the next player, "O". And vice versa.
        if choice.upper() == "X":
            choice = "O"
        else:
            choice = "X"

        #the current turn is over. Increase the count of turns taken by 1
        turns += 1

        #If Player 1 is X and there are 3 X's in a valid tic-tac-toe row, then Player 1 is declared winner and game ends
        if ((orig_choice == "X") and
            ((board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or
             (board['4'] == "X" and board['5'] == "X" and board['6'] == "X") or
             (board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or
             (board['7'] == "X" and board['4'] == "X" and board['1'] == "X") or
             (board['8'] == "X" and board['5'] == "X" and board['2'] == "X") or
             (board['9'] == "X" and board['6'] == "X" and board['3'] == "X") or
             (board['7'] == "X" and board['5'] == "X" and board['3'] == "X") or
             (board['9'] == "X" and board['5'] == "X" and board['1'] == "X"))):
            print("Player 1 wins")
            break
        #If Player 1 is O and there are 3 O's in a valid tic-tac-toe row, then Player 1 is declared winner and game ends
        elif ((orig_choice == "O") and
              ((board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or
               (board['4'] == "O" and board['5'] == "O" and board['6'] == "O") or
               (board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or
               (board['7'] == "O" and board['4'] == "O" and board['1'] == "O") or
               (board['8'] == "O" and board['5'] == "O" and board['2'] == "O") or
               (board['9'] == "O" and board['6'] == "O" and board['3'] == "O") or
               (board['7'] == "O" and board['5'] == "O" and board['3'] == "O") or
               (board['9'] == "O" and board['5'] == "O" and board['1'] == "O"))):
            print("Player 1 wins")
            break
        #If Player 1 is not X and there are 3 X's in a valid tic-tac-toe row, then Player 2 is declared winner and game ends
        elif ((orig_choice != "X") and
              ((board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or
               (board['4'] == "X" and board['5'] == "X" and board['6'] == "X") or
               (board['1'] == "X" and board['2'] == "X" and board['3'] == "X") or
               (board['7'] == "X" and board['4'] == "X" and board['1'] == "X") or
               (board['8'] == "X" and board['5'] == "X" and board['2'] == "X") or
               (board['9'] == "X" and board['6'] == "X" and board['3'] == "X") or
               (board['7'] == "X" and board['5'] == "X" and board['3'] == "X") or
               (board['9'] == "X" and board['5'] == "X" and board['1'] == "X"))):
            print("Player 2 wins")
            break
        #If Player 1 is not O and there are 3 O's in a valid tic-tac-toe row, then Player 2 is declared winner and game ends
        elif ((orig_choice != "O") and
              ((board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or
               (board['4'] == "O" and board['5'] == "O" and board['6'] == "O") or
               (board['1'] == "O" and board['2'] == "O" and board['3'] == "O") or
               (board['7'] == "O" and board['4'] == "O" and board['1'] == "O") or
               (board['8'] == "O" and board['5'] == "O" and board['2'] == "O") or
               (board['9'] == "O" and board['6'] == "O" and board['3'] == "O") or
               (board['7'] == "O" and board['5'] == "O" and board['3'] == "O") or
               (board['9'] == "O" and board['5'] == "O" and board['1'] == "O"))):
            print("Player 2 wins")
            break
        else:
            if (turns == 10): #If the number of turns is equal to 9 (max # of turns in a game) and there has been no winner
                print("It is a draw!") #declare the game a draw and end it
                break
            else: #otherwise continue the game
                continue
    replay() #calls the replay function

#calling the tic tac toe function, which begins the game
ticTacToe()

