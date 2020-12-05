#!python3
from helpers.read_lines import *
from typing import List, Tuple
input = read_line_input("day5")

def bsearch(letter:str, min:int, max:int) -> Tuple:
    if letter == "F" or letter == "L":
        #do the lower half
        return min, (max+min)//2
    else:
        return ((max+min)//2)+1, max

def find_row(row:str) -> int:
    min = 0
    max = 127
    for letter in row:
        min, max = bsearch(letter, min, max)
    return min

def find_col(col:str) -> int:
    min = 0
    max = 7
    for letter in col:
        min, max = bsearch(letter, min, max)
    return min

def missing_elements(L):
    start, end = L[0], L[-1]
    return set(range(start, end + 1)).difference(L)

def run():
    seat_ids = []
    for line in input:
        line = line.strip()
        row = line[:7]
        col = line[7:]
        row_num = find_row(row)
        col_num = find_col(col)
        seat_ids.append(row_num * 8 + col_num)

    print(f"Max seat id: {max(seat_ids)}")
    seat_ids.sort()
    print(missing_elements(seat_ids))
