from board import DefenseBoard, AttackBoard, SimulationBoard
import numpy as np
import random 

# Class that handles interaction between agent and environment
class Game:
    def __init__(self, size, ships):
        self.size = size  # Size of board, i.e. size * size = total squares
        self.ships = ships
        self.defense_board = DefenseBoard(self.size, self.ships)  # Initialise a new DefenseBoard 
        self.attack_board = AttackBoard(self.defense_board)  # Initialise a new AttackBoard 
        self.simulate_board = SimulationBoard(self.attack_board)  # Initialise a new SimulationBoard

        self.attack_board.print_board("=Initial State=")
        self.count = 0

    # Return the initial state
    def reset(self):
        self.__init__(self.size, self.ships)
        return self.attack_board

    # Takes a step in the environment
    def step(self, probs):
        # strategy = 'random'
        strategy = 'probabilistic'

        if strategy == "probabilistic":
            x, y = np.unravel_index(probs.argmax(), probs.shape)

            while not self.attack_board.legal_hit(x, y):
                probs[x, y] = 0
                x, y = np.unravel_index(probs.argmax(), probs.shape)
        else:
            x, y = random.choice(range(10)), random.choice(range(10))

        outcome, done = self.attack_board.send_hit(x, y)

        return self.attack_board, outcome, done



