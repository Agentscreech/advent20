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

def p1():
    x = 0
    y = 0
    cur_dir = "E"
    directions = parse_input(input)
    move_ship = {
        "N": N,
        "S": S,
        "W": W,
        "E": E
    }
    left = {
        "N": "W",
        "W": "S",
        "S": "E",
        "E": "N"
    }    
    right = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }
    for d in directions:
        if d[0] == "L":
            for _ in range((d[1]//90)):
                cur_dir = left[cur_dir]
            continue
        if d[0] == "R":
            for _ in range((d[1]//90)):
                cur_dir = right[cur_dir]
            continue
        if d[0] in ["N", "W", "S", "E"]:
            x, y = move_ship[d[0]](x, y, d[1])
            continue
        x, y = move_ship[cur_dir](x, y, d[1])
    print(abs(x)+abs(y))
        
    #N = -x
#W = -y    #E = +y
     #S = +x
