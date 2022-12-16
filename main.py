from game_env_interface import Game
from ai import AI
from utils import letter_to_coords
import argparse

import numpy as np

winner = {(True, False): 'Computer',
          (False, True): 'Player'}

def init_game(size, ships, samples):

    strategy = ["probabilistic", "random"]

    ai_env = Game(size, ships)
    computer = AI(ai_env, samples)
    player_env = Game(size, ships)

    # Keep playing until one of the players has won
    c_done = False
    p_done = False
    while not c_done and not p_done:
        c_state, c_outcome, c_done = computer.move()
        p_state, p_outcome, p_done = player_env.step(execute_player_move(player_env))

        c_state.print_board(f"=Your Board (Computer Target Ships)= [Last Outcome: {c_outcome}]")
        p_state.print_board(f"=Your Target Ships= [Last Outcome: {p_outcome}]")

    print("="*10 + "GAME OVER" + "="*10)
    print(f"The winner is: {winner[(c_done, p_done)]}")


# Get the input move from the player
def execute_player_move(player_env):
    p_move = np.zeros(shape=[player_env.size, player_env.size])
    x, y = player_input(player_env)
    p_move[x, y] = 1
    return p_move

# Validate the player move
def player_input(player_env):
    success = False
    while not success:
        ltr, nbr = input("Enter letter: ").upper(), input("Enter number: ") # Get the input from the player
        try:
            x, y = letter_to_coords(ltr, nbr)
            while player_env.attack_board.get_board()[x, y] != 0: # Check if the move has already been made
                x, y = player_input()
            success = True
        except:
            print("Invalid Input!") # If the input is invalid, ask for input again
            continue
    return x, y


if __name__ == '__main__':
    parser = argparse.ArgumentParser() # Parse the arguments
    parser.add_argument('--board_size', help='The size of the board, default: 10', default=10) 
    parser.add_argument('--ship_sizes', help='Array of ship sizes to randomly place, default: "5,4,3,3,2"', default='5,4,3,3,2')
    parser.add_argument('--monte_carlo_samples', help='The number of samples to get the algorithm to do, default: 10000', default=10000)

    args = parser.parse_args()

    try:
        print("Chosen args: ", args.board_size, [int(x) for x in args.ship_sizes.split(',')], args.monte_carlo_samples)
        init_game(args.board_size, [int(x) for x in args.ship_sizes.split(',')], args.monte_carlo_samples)
    except:
        print("Incorrect Args!")
        exit(1)
