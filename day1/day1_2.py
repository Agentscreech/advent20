#!python3
from helpers.read_lines import *
from typing import List, Tuple
from itertools import combinations
numbers = read_line_input("day1")

#find the 3 numbers in the list that add to 2020

#get all possible combinations
combs = combinations(numbers, 3)

def return_product(numbers: Tuple[str,str,str]) -> int:
    return int(numbers[0]) * int(numbers[1]) * int(numbers[2])

def check_for_2020(numbers: Tuple[str,str,str]) -> bool:
    if int(numbers[0]) + int(numbers[1]) + int(numbers[2]) == 2020:
        return True
    else:
        return False

def run():
    for c in combs:
        if check_for_2020(c):
            print(return_product(c))
            break
