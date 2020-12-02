#!python3
from helpers.read_lines import *
from typing import List
input = read_line_input("day2")


def parse_line(line:str) -> List:
    parts = line.split(" ")
    min = int(parts[0].split('-')[0])
    max = int(parts[0].split('-')[1])
    letter = parts[1][0]
    code = parts[2]
    return [min, max, letter, code]


def check_code(min:int, max:int, letter:str, code:str) -> bool:
    count = 0
    for l in code:
        if l == letter:
            count += 1
    if count >= min and count <= max:
        return True
    return False



def run():
    correct = 0
    for line in input:
        #cut up the input in to the things we need to work with 
        min, max, letter, code = parse_line(line)
        if check_code(min, max, letter, code):
            correct += 1
    print(correct)

