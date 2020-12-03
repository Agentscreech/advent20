#!python3
from helpers.read_lines import *
from typing import List
input = read_line_input("day3")


def by_two(move_right:int) -> int:
    counter = 0
    length = len(input[0].strip())
    x_pos = 0
    trees = 0
    for line in input[2:]:
        if counter % 2 == 1:
            counter += 1
            continue
        line = line.strip()
        x_pos += move_right
        if line[x_pos % length] == "#":
            trees += 1
        counter += 1
    return trees


def by_one(move_right:int) -> int:
    length = len(input[0].strip())
    x_pos = 0
    trees = 0
    for line in input[1:]:
        line = line.strip()
        x_pos += move_right
        if line[x_pos % length] == "#":
            trees += 1
    return trees

def run():
    total = by_two(1)
    for move in [1,3,5,7]:
        total *= by_one(move)
    print(total)