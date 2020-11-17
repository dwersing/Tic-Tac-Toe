from IPython.display import clear_output, display
import random


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_name():
    name1 = input('Player 1, Enter your name: ')
    print('Good Luck ' + name1)
    name2 = input('Player 2, Enter your name: ')
    print('Good Luck ' + name2)

    return name1, name2


def place_marker():
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ').upper()

    if marker == 'X':
        return 'X', 'O'

    else:
        return 'O', 'X'


def renamed_function(board, marker, position):
    board[position] = marker


def check_winner(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark))


def first_move():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def position_open(board, position):
    return board[position] == ' '


def position_not_open(board):
    for i in range(1, 10):
        if position_open(board, i):
            return False
    return True


def player_next_move(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not position_open(board, position):
        position = int(input('Please enter your next move (1-9) '))
    return position


def replay():
    return input('Do you want to play again?  Enter Yes or No: ').lower().startswith('y')


print('Welcome and thank you for playing Tic Tac Toe!')

while True:
    board = [' '] * 10
    player_name1, player_name2 = player_name()
    player1, player2 = place_marker()
    turn = first_move()
    print(turn + ' will make the first move')

    play_game = input('Are you ready to begin?')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_next_move(board)
            renamed_function(board, player1, position)

            if check_winner(board, player1):
                display(board)
                print('Congratulations ' + player_name1 + '!  You won the game!')
                game_on = False
            else:
                if position_not_open(board):
                    display_board(board)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            position = player_next_move(board)
            renamed_function(board, player2, position)

            if check_winner(board, player2):
                display(board)
                print('Congratulations ' + player_name2 + '!  You won the game!')
                game_on = False
            else:
                if position_not_open(board):
                    display_board(board)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
