import numpy as np


# Place a random ship on the given board of the given length, making sure it does not intersect
def place_random_ship(board, length, no_intersect):
    placed = False
    while not placed:
        vertical = bool(np.random.randint(0, 2))  

        # Make sure the ship will be on the board
        o1 = o2 = 0
        while abs(o1 - o2) != length - 1:
            s, o1, o2 = np.random.randint(0, board.size), np.random.randint(0, board.size), np.random.randint(0,
                                                                                                            board.size)
        # Make sure the ship will be a horizontal or vertical line
        if vertical:
            y1 = y2 = s
            x1 = o1
            x2 = o2
        else:
            x1 = x2 = s
            y1 = o1
            y2 = o2

        # Make sure the ship does not intersect another existing ship
        try:
            ship_crds = place_ship(board, x1, y1, x2, y2, no_intersect)
            board.ships.append(ship_crds)
            placed = True
        except AssertionError:
            continue


def place_ship(board, x1, y1, x2, y2, no_intersect):
    # Make sure the ship will be a horizontal or vertical line
    assert x1 == x2 or y1 == y2, "Coordinates must be inline"
    # Make sure the ship is not of size one
    assert not (x1 == x2 and y1 == y2), "Cannot be one point"
    # Make sure all coords are on the board
    for cd in [x1, x2, y1, y2]:
        assert 0 <= cd < board.size, f"{cd} is not on board"

    # Sort the coords
    smallest_x, greatest_x = sorted([x1, x2])[0], sorted([x1, x2])[1]
    smallest_y, greatest_y = sorted([y1, y2])[0], sorted([y1, y2])[1]

    # Make sure the ship does not intersect another existing ship
    for x in range(smallest_x, greatest_x + 1):
        for y in range(smallest_y, greatest_y + 1):
            assert board.get_board()[x, y] not in no_intersect, "Invalid intersection"

    # Place the ship
    coords = []
    for x in range(smallest_x, greatest_x + 1):
        for y in range(smallest_y, greatest_y + 1):
            board.get_board()[x, y] = board.inv_square_states['ship']
            coords.append((x, y))

    return coords

# Convert a letter and number to coordinates
def letter_to_coords(letter, number):
    letter_coord = ord(letter) - 65
    number_coord = int(number) - 1
    return letter_coord, number_coord
