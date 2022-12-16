# Battleships AI

## Introduction

This is a version of the game Battleships in which two players attempt to sink all of their opponents ships first. 
Here, you play vs an AI, which works through [Monte Carlo Simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method). 
Originally this project was designed to build a neural reinforcement learning agent to play the game, however I have been
unsuccessful in this goal so far. If anyone reading this has any ideas of how to go about such a thing, I would love to hear them!

## Monte Carlo Simulation

### Description

The basics of how it works are as follows:

1. Take current board state as input
2. Create copy of board state
3. Simulate a specific number of samples (given by `--monte_carlo_samples`), each of which is a random placement of a remaining ship type
4. Stack all of the simulations and sum the total number of ships in each square (emphasise ships that overlap existing hits)
5. Take the mean for each sqaure, giving us a frequency matrix or heatmap
5. Pick the largest value corresponding to a legal move in the matrix
6. Repeat

### Heatmap

[There are two heatmap gifs](https://github.com/DataSnaek/battleships_ai/tree/master/heatmap_gifs) in this project which demonstrate the probability matrix as a heatmap for every square after each move in the game. Here is one of them:

![heatmap](https://github.com/DataSnaek/battleships_ai/blob/master/heatmap_gifs/battleships_2.gif)

## Prerequisites

### Packages

Done entirely using the `python 3.6` standard library, with the exception of `numpy` which is required.

### Instructions

The `main.py` file takes 3 arguments as follows:

* `--board_size`: The size of the board, default: `10`
* `--ship_sizes`: Array of ship sizes to randomly place, default: `5,4,3,3,2`
* `--monte_carlo_samples`: The number of samples to get the algorithm to do, default: `10000`

If you have a slow computer, choose a lower number of samples, but generally 10,000 should get good results in decent time. 
Make sure not to put spaces between the integers in ship_sizes. 
Extemely large or small board sizes may have unexpected behaviour, generally the safe range is 5-10, but with appropriate adjustments to the other parameters, sizes outwith this range will work fine.

Once run, the game will initialise two boards of ships randomly (choosing ship locations is not implemented currently), one for you and one for the computer. The key for square types is as follows:

* Sea: ■
* Hit: X
* Miss: □
* Destroyed: *

The player goes first and specifies a move by giving first a letter and then a number to determine the target square.


## License

This project is released under the MIT license, see LICENSE.md for more details.