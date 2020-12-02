#!python3
from helpers.read_lines import *
from typing import List
input = read_line_input("day2")


def parse_line(line: str) -> List:
    parts = line.split(" ")
    pos1 = int(parts[0].split('-')[0])
    pos2 = int(parts[0].split('-')[1])
    letter = parts[1][0]
    code = parts[2].strip()
    return [pos1, pos2, letter, code]


def check_code(pos1: int, pos2: int, letter: str, code: str) -> bool:
    count = 0
    if code[pos1-1] == letter:
        count += 1
    if code[pos2-1] == letter:
        count += 1
    if count == 1:
        return True
    return False

def run():
    correct = 0
    for line in input:
        #cut up the input in to the things we need to work with
        pos1, pos2, letter, code = parse_line(line)
        if check_code(pos1, pos2, letter, code):
            correct += 1
    print(correct)
