#!/usr/bin/env python3
##
## Fruition Sciences, 2023
## vacuum's positions
## File description:
## Test_technique_mehrdad_Zeinali
##

def move_forward(position, orientation):
    x, y = position
    if orientation == "N":
        return (x, y + 1)
    elif orientation == "S":
        return (x, y - 1)
    elif orientation == "E":
        return (x + 1, y)
    elif orientation == "W":
        return (x - 1, y)

def rotate(orientation, direction):
    if direction == "D":
        if orientation == "N":
            return "E"
        elif orientation == "E":
            return "S"
        elif orientation == "S":
            return "W"
        elif orientation == "W":
            return "N"
    elif direction == "G":
        if orientation == "N":
            return "W"
        elif orientation == "W":
            return "S"
        elif orientation == "S":
            return "E"
        elif orientation == "E":
            return "N"

def run_commands(commands, position, orientation, grid_size):
    x_max, y_max = grid_size
    for command in commands:
        if command == "A":
            next_position = move_forward(position, orientation)
            x, y = next_position
            if x >= 0 and x <= x_max and y >= 0 and y <= y_max:
                position = next_position
        else:
            orientation = rotate(orientation, command)
    return position, orientation

grid_size = tuple(map(int, input().split()))
val = input().split()
position = tuple(map(int, val[:2]))
orientation = val[2]
commands = input().strip()

final_position, final_orientation = run_commands(commands, position, orientation, grid_size)
print(" ".join(map(str, final_position)) + " " + final_orientation)
