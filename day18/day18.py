#!python3
import copy
from collections import deque
from helpers.read_lines import *
from typing import List, Tuple
input = read_line_input("day18")


def parse_data(input):
    output = []
    for line in input:
        line = line.strip()
        output.append(line)
    return output


sample1 = [
    "2 * 3 + (4 * 5)", # becomes 26.",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)", # becomes 437.",
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", # becomes 12240.",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",# becomes 13632.",
]

def linear_solver(eq:str) -> int:
    total = 0
    next_math = "+"
    operations = eq.split(" ")
    for i in operations:
        try:
            if int(i):
                if next_math == "+":
                    total += int(i)
                elif next_math == "*":
                    total *= int(i)
        except:
            next_math = i
    return total

def sum_first(eq:str) -> int:
    total = 1
    #find all the things to add first, then multiply the remaining results
    sums = eq.split(" ")
    plus_indices = [i for i, x in enumerate(sums) if x == "+"]
    #replace the summed number in place in the array
    for i, plus in enumerate(plus_indices):
        if i > 0:
            plus -= i+i
        sums[plus] = int(sums[plus-1])+int(sums[plus+1])
        del sums[plus+1]
        del sums[plus-1]
    #mulitply the rest of the added up numbers
    for i in sums:
        if i != "*":
            total *= int(i)
    return total

def p_finder(eq:str, mode:str) -> int:
    count = 0
    start = 0
    end = 0
    sub_eq = ""
    base_eq = ""
    for c in eq:
        if c == "(":
            if start == 0:
                start += 1
            else:
                start += 1
                sub_eq += c
        elif c == ")":
            end += 1
            if start == end:
                base_eq += str(p_finder(sub_eq, mode))
                sub_eq = ""
                start = 0
                end = 0
                continue
            sub_eq += c
        elif start > 0:
            sub_eq += c
        elif start == 0:
            base_eq += c
    if mode == "l":
        count += linear_solver(base_eq)
    elif mode == "s":
        count += sum_first(base_eq)
    return count
        
            
            
def p1():
    #parse out the parenstheses then solve left to right
    total = 0
    for line in parse_data(input):
        total += p_finder(line, "l")
    print(total)

def p2():
    total = 0 
    for line in parse_data(input):
        total += p_finder(line, "s")
    print(total)



