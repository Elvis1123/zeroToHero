import random


def display_board(board):
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')


def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('Choose X or O').upper()

    if marker == 'X':
        return ('X', 'O')
    if marker == 'O':
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if (board[1] == mark and board[2] == mark and board[3] == mark):
        return True
    elif (board[4] == mark and board[5] == mark and board[6] == mark):
        return True
    elif (board[7] == mark and board[8] == mark and board[9] == mark):
        return True
    elif (board[1] == mark and board[4] == mark and board[7] == mark):
        return True
    elif (board[2] == mark and board[5] == mark and board[8] == mark):
        return True
    elif (board[3] == mark and board[6] == mark and board[9] == mark):
        return True
    elif (board[1] == mark and board[5] == mark and board[9] == mark):
        return True
    elif (board[3] == mark and board[5] == mark and board[7] == mark):
        return True
    else:
        return False


def choose_first():
    x = random.randint(1,2)
    return x

def space_check(board, position):
    if (board[position]=='X'or board[position]=='O'):
        return False
    else:
        return True

def full_board_check(board):
    add = True
    while add:
        for i in range(1,9):
            if(board[i]=='X' or board[i]=='O'):
                add = True
            else:
                add = False
                return add
                break
        else:
            return add

def player_choice(board):
    position = int(input('Your next move'))
    lst = []
    while (position in range(1, 10)):
        if space_check(board, position):
            return position
        else:
            position = int(input('Your next move, again'))
    else:
        position = int(input('Your next move, again'))


def replay():
    replay = input('Do you want to play again [Y/N]').upper()
    return replay == 'Y'

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')

    while True:
        theboard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        player1_mark, player2_mark = player_input()

        turn = choose_first()
        print('Player {} will go first'.format(turn))

        play_game = input('Are you ready to play [Y/N]')
        if play_game.upper() == 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if (turn == 1):
                display_board(theboard)
                position = player_choice(theboard)
                place_marker(theboard, player1_mark, position)
                if win_check(theboard, player1_mark):
                    print('Player 1 has won. Congratulations')
                    display_board(theboard)
                    game_on = False
                else:
                    if full_board_check(theboard):
                        print('Nobody won')
                        display_board(theboard)
                        break
                    else:
                        turn = 2
            else:
                display_board(theboard)
                position = player_choice(theboard)
                place_marker(theboard, player2_mark, position)
                if win_check(theboard, player2_mark):
                    print('Player 2 has won. Congratulations')
                    display_board(theboard)
                    game_on = False
                else:
                    if full_board_check(theboard):
                        print('Nobody won')
                        display_board(theboard)
                        break
                    else:
                        turn = 1

        if not replay():
            break