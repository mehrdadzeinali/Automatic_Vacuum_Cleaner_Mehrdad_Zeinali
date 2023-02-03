#!/usr/bin/env python3
##
## Fruition Sciences, 2023
## vacuum's positions
## File description:
## Test_technique_mehrdad_Zeinali
##

def move_forward(position, orientation):
    x, y = position
    cases = {
        "N": (x, y + 1),
        "S": (x, y - 1),
        "E": (x + 1, y),
        "W": (x - 1, y)
    }
    return cases.get(orientation, position)

def rotate(orientation, direction):
    cases = {
        "N": {"D": "E", "G": "W"},
        "E": {"D": "S", "G": "N"},
        "S": {"D": "W", "G": "E"},
        "W": {"D": "N", "G": "S"},
    }
    return cases[orientation].get(direction, orientation)

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
