#########Global Veriables##########
#board
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-',]

game_still_going = True

winner = None

current_player = 'X'

#display the board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():
    #displays inital board
    display_board()
    #while game_still_going = True
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()
    #once game_still_going = False
    if winner == 'X' or winner == 'O':
        print()
        print('The winner is ', winner)
    else:
        print()
        print('TIE')


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    #declare the global veriable
    global winner
    #check rows
    row_winner = check_rows()
    #check_colums
    column_winner = check_columns()
    #check_diag
    diaganal_winner = check_diag()
    #get the winner
    if row_winner:
        #there is a win
        winner = row_winner
    elif column_winner:
        #there is a win
        winner = column_winner
    elif diaganal_winner:
        #ther is a winner
        winner = diaganal_winner
    else:
        #there is no winner
        winner = None
    return


#checks rows for a winner
def check_rows():

    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    #return the winner
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

#checks columns for winner
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    #returns winner
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


#checks diaganals for winner
def check_diag():
    global game_still_going
    diaganal_1 = board[0] == board[4] == board[8] != '-'
    diaganal_2 = board[6] == board[4] == board[2] != '-'

    if diaganal_1 or diaganal_2:
        game_still_going = False
    if diaganal_1:
        return board[0]
    elif diaganal_2:
        return board[6]



def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return

#responsible for taking turns
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return


def handle_turn(current_player):

    print(current_player + "'s turn.")
    position = input('Choose a position, 1-9 ')

    valid = False
    #runs until valid = True
    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Not a valid input, choose a position 1-9 ')

        position = int(position) - 1
        #returns valid = False if spot already taken
        if board[position] == '-':
            valid = True

        else:
            print('That space is taken! Go again')
    #places 'X' or 'O' and displays board
    board[position] = current_player
    print(display_board())

#main program
play_game()
#calls empty board

#play the game
#handle turn
#check win
    #check rows
    #check coloms
    #check diaganal
#check tie
#flip player
