#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## example.py
## File description:
## -
##

import math

def move_forward(position, orientation, angle, distance):
    x, y = position
    x = int(x)
    y = int(y)
    radians = math.radians(angle)
    cases = {
        "N": (x, int(y + distance * math.sin(radians))),
        "S": (x, int(y - distance * math.sin(radians))),
        "E": (int(x + distance * math.sin(radians)), y),
        "W": (int(x - distance * math.sin(radians)), y)
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
            next_position = move_forward(position, orientation, 90, 1)
            x, y = next_position
            if x >= 0 and x <= x_max and y >= 0 and y <= y_max:
                position = next_position
        else:
            orientation = rotate(orientation, command)
    return position, orientation

while True:
    try:
        grid_size = tuple(map(int, input().split()))
        if len(grid_size) != 2:
            raise ValueError("The first line must contain 2 digits with a space between them.")
        val = input().split()
        position = tuple(map(int, val[:2]))
        orientation = val[2]
        if len(position) != 2 or len(orientation) != 1 or orientation not in ['N', 'E', 'S', 'W']:
            raise ValueError("The second line must contain 2 numbers and an uppercase orientation (N, E, S or W).")
        commands = input().strip()
        if not all(c in ['A', 'D', 'G'] for c in commands):
            raise ValueError("The third line must contain only 'A', 'D' and 'G'.")
        final_position, final_orientation = run_commands(commands, position, orientation, grid_size)
        print(" ".join(map(str, final_position)) + " " + final_orientation)
        break
    except Exception as e:
        print(e)
        continue
