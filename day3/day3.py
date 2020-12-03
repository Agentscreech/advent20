#!python3
from helpers.read_lines import *
from typing import List
input = read_line_input("day3")

def run():
    length = len(input[0].strip())
    x_pos = 0
    trees = 0
    for line in input[1:]:
        line = line.strip()
        x_pos += 3
        if line[x_pos % length] == "#":
            trees += 1
    print(trees)


