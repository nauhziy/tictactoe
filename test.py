"""
A simple python tic-tac-toe game
"""

import os
import ldclient
import random
from ldclient.config import Config
from dotenv import load_dotenv


# Pull secrets from .env file
load_dotenv()
sdk_key = os.getenv('sdk_key')


def print_board(board_dict, player_icon, player_1, player_2):
    print(f"\n{player_1}: {player_icon[1]} {player_2}: {player_icon[2]}")

    print('\n    1 -- 2 -- 3')
    print('a :', board_dict['a1'], '|', board_dict['a2'], '|', board_dict['a3'])
    print('   -----------')
    print('b :', board_dict['b1'], '|', board_dict['b2'], '|', board_dict['b3'])
    print('   -----------')
    print('c :', board_dict['c1'], '|', board_dict['c2'], '|', board_dict['c3'])

    pass


def print_winner(check, board_dict, player_icon, player_1, player_2):
    print_board(board_dict, player_icon, player_1, player_2)
    print('Game Over!')

    if board_dict[check] == player_icon[1]:
        print(f'{player_1} is the tic-tac-toe champion!!!')
    else:
        print(f'{player_2} is the tic-tac-toe champion!!!')

def check_win(board_dict, player_icon, player_1, player_2):

    if board_dict['a1'] == board_dict['a2'] == board_dict['a3'] != ' ':
        print_winner('a1', board_dict, player_icon, player_1, player_2)
        return True

    elif board_dict['b1'] == board_dict['b2'] == board_dict['b3'] != ' ':
        print_winner('b1', board_dict, player_icon, player_1, player_2)
        return True

    elif board_dict['c1'] == board_dict['c2'] == board_dict['c3'] != ' ':
        print_winner('c1', board_dict, player_icon, player_1, player_2)
        return True

    elif board_dict['a1'] == board_dict['b1'] == board_dict['c1'] != ' ':
        print_winner('a1', board_dict, player_icon, player_1, player_2)
        return True

    elif board_dict['a2'] == board_dict['b2'] == board_dict['c2'] != ' ':
        print_winner('a2', board_dict, player_icon, player_1, player_2)
        return True

    elif board_dict['a3'] == board_dict['b3'] == board_dict['c3'] != ' ':
        print_winner('a3', board_dict, player_icon, player_1, player_2)
        return True

    elif board_dict['a1'] == board_dict['b2'] == board_dict['c3'] != ' ':
        print_winner('a1', board_dict, player_icon, player_1, player_2)
        return True

    elif board_dict['a3'] == board_dict['b2'] == board_dict['c1'] != ' ':
        print_winner('a3', board_dict, player_icon, player_1, player_2)
        return True

    return False


def game(board_dict, player_1, player_2):
    player_turn = ''
    player_icon = {}
    count = 0

    if random.random() <= 0.5:
        print(f"Coin flipped - {player_1} starts with X!")
        player_turn = player_1
        player_icon[1] = 'X'
        player_icon[2] = 'O'

    else:
        print(f"Coin flipped - {player_2} starts with X!")
        player_turn = player_2
        player_icon[1] = 'O'
        player_icon[2] = 'X'

    while count < 9:
        print_board(board_dict, player_icon, player_1, player_2)

        print(f"\nIt's {player_turn}'s turn. What's your next move?")

        move = input()

        if board_dict.get(move, None) is None:
            print(f'{move} is not a valid move!')
            print(f'Please type something with the axis values')
            print(f'e.g. a1')
            continue

        elif board_dict.get(move, None) == ' ':
            if player_turn == player_1:
                board_dict[move] = player_icon[1]
            else:
                board_dict[move] = player_icon[2]
            count += 1
        else:
            print("That place is already filled.\n Try again!")
            continue

        if check_win(board_dict, player_icon, player_1, player_2):
            break

        # Now we have to change the player after every move.
        if player_turn == player_1:
            player_turn = player_2
        else:
            player_turn = player_1

    if count == 9 and not check_win(board_dict, player_icon, player_1, player_2):
        print("It's a tie...")

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key, value in board_dict.items():
            board_dict[key] = " "

        game(board_dict, player_1, player_2)


if __name__ == "__main__":
    ldclient.set_config(Config(sdk_key))

    user = {
        "key": "UNIQUE IDENTIFIER",
        "firstName": "Yi Zhuan",
        "lastName": "Foong",
        "custom": {
            "groups": "takehome_test"
        }
    }

    show_feature = ldclient.get().variation("test-flag", user, False)

    # initialize the board
    board_dict = {'a1': ' ', 'a2': ' ', 'a3': ' ',
                  'b1': ' ', 'b2': ' ', 'b3': ' ',
                  'c1': ' ', 'c2': ' ', 'c3': ' '}

    if show_feature:
        print("Let's play OMG WHAT IS GOING ON?????!!!!! tic-tac-toe!")
    else:
        print("Let's play tic-tac-toe!")

    player_1 = input("Player 1, what's your name?\n")
    player_2 = input("Player 2, what's your name?\n")

    game(board_dict, player_1, player_2)

    ldclient.get().close()
