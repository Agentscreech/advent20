#!python3
import copy
from helpers.read_lines import *
from typing import List, Tuple
input = read_line_input("day12")


sample1 = [
    "F10",
    "N3",
    "F7",
    "R90",
    "R90",
    "R90",
    "R90",
    "L90",
    "L90",
    "L90",
    "L90",
    "R90",
    "F11"
]


def parse_input(input):
    output = []
    for line in input:
        output.append((line[0], int(line[1:])))
    return output


def N(x, y, steps):
    return x, y+steps


def S(x, y, steps):
    return x, y-steps


def W(x, y, steps):
    return x-steps, y


def E(x, y, steps):
    return x+steps, y

def run():
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1
    directions = parse_input(input)
    move_waypoint = {
        "N": N,
        "S": S,
        "W": W,
        "E": E
        }
    for d in directions:
        if d[0] == "L":
            for _ in range((d[1]//90)):
                way_x, way_y = -way_y, way_x
            continue
        if d[0] == "R":
            for _ in range((d[1]//90)):
                way_x, way_y = way_y, -way_x
            continue
        if d[0] in ["N", "W", "S", "E"]:
            way_x, way_y = move_waypoint[d[0]](way_x, way_y, d[1])
            continue
        #F
        ship_x += way_x * d[1]
        ship_y += way_y * d[1]
    print(abs(ship_x)+abs(ship_y))
