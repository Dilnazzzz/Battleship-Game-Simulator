from utils import *
import threading, os
import numpy as np
import matplotlib.pyplot as plt


# Class dor two algorithms for AI
class AI:
    def __init__(self, env, samples):
        self.env = env # The environment to run the AI
        self.move_sim = samples  # The number of moves to simulate
        self.priority = 5  # The priority to give simulations that intersect hits

    # Evaluate the model by finding the mean score over a number of games
    def eval_model(self, evals): # evals = number of games to play
        scores = [] # List of scores
        for i in range(evals): # For each game
            scores.append(self.run(i)) # Run the game and append the score
            print(f"Game {i}/{evals} \n Score: {scores[-1]}") 
        print(np.mean(scores))

    # Return probability matrix
    def monte_carlo(self, state, out_path): # out_path = path to save heatmap
        simulations = []

        #
        for i in range(self.move_sim):
            self.env.simulate_board.update(state) # Update the simulation board
            brd, intersect = self.env.simulate_board.simulate_ship()

            # If we intersect a hit, take into account priority and overlap with the ship
            if intersect:
                for i in range(self.priority):
                    for i in range(intersect):
                        simulations.append(brd) # Add the ship to the simulations
            simulations.append(brd)

        # Get the mean of the simulations
        simulations = np.array(simulations)
        percentages = np.mean(simulations, axis=0)

        # Output a heatmap if specified by out_path
        if out_path != '':
            fig = plt.figure(figsize=(8, 8))
            fig.add_subplot(1, 2, 1)
            plt.imshow(percentages, cmap='hot', interpolation='nearest') # Plot the heatmap
            fig.add_subplot(1, 2, 2)
            plt.imshow(state.get_board() * 5, cmap='bwr', interpolation=None)
            plt.savefig(out_path) # Save the heatmap in the specified directory 
            plt.close(fig)

        return percentages

    # Run a game for testing 
    def run(self, r_count):
        s = self.env.reset() # Reset the environment
        done = False
        count = 0
        while not done:
            count += 1
            if not os.path.exists(f'save_file_{r_count}/'): # Create a directory to save the heatmaps
                os.mkdir(f'save_file_{r_count}/')
            s, done = self.env.step(self.monte_carlo(s, f'save_file_{r_count}/{count}.png')) # Take a step in the environment
            # s.print_board()
        print(f"SCORE: {np.count_nonzero(s.get_board() == 0)}") 
        return np.count_nonzero(s.get_board() == 0)

    # Predict a move against a player and make that move
    def move(self):        return self.env.step(self.monte_carlo(self.env.attack_board, '/Users/dilnaz/Documents/app/battleships_ai/heatmap_gifs/heatmap.png'))



