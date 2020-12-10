#!python3
import collections
from helpers.read_lines import *
from typing import List
input = read_line_input("day10")


def parse_input(input) -> List:
    numbers = []
    for line in input:
        numbers.append(int(line.strip()))
    return numbers

sample1 = [
    "16",
    "10",
    "15",
    "5",
    "1",
    "11",
    "7",
    "19",
    "6",
    "12",
    "4"
]

sample2 = [
    "28",
    "33",
    "18",
    "42",
    "31",
    "14",
    "46",
    "20",
    "48",
    "47",
    "24",
    "23",
    "49",
    "45",
    "19",
    "38",
    "39",
    "11",
    "1",
    "32",
    "25",
    "35",
    "8",
    "17",
    "7",
    "9",
    "4",
    "2",
    "34",
    "10",
    "3"
]
def next_adapter(numbers:List,current:int) -> int:
    if current + 1 in numbers:
        return 1, current+1
    if current + 2 in numbers:
        return 2, current+2
    if current + 3 in numbers:
        return 3, current+3

    

def p1():
    numbers = parse_input(input)
    top_jolt = max(numbers)
    numbers.sort()
    numbers.append(top_jolt+3)
    current = 0
    one_jumps = 0
    two_jumps = 0
    three_jumps = 0
    print(numbers)
    for _ in range(len(numbers)):
        jump, current = next_adapter(numbers, current)
        if jump == 1:
            one_jumps += 1
        if jump == 2:
            two_jumps += 1
        if jump == 3:
            three_jumps += 1
    print(one_jumps, two_jumps, three_jumps)
    print(one_jumps * three_jumps)

def get_branches(numbers, current):
    branch_nums = []
    if current + 1 in numbers:
        branch_nums.append(current + 1)
    if current + 2 in numbers:
        branch_nums.append(current + 2)
    if current + 3 in numbers:
        branch_nums.append(current + 3)
    return branch_nums

def p2():
    numbers = [0]
    numbers.extend(parse_input(input))
    top_jolt = max(numbers)
    numbers.sort()
    numbers.append(top_jolt+3)
    number_totals = {}
    branches = []
    for current_num in numbers:
        sub_branches = (get_branches(numbers,current_num))
        branches.append((current_num, sub_branches))

    for branch in branches[::-1]:
            subtotal = 0
            num = branch[0]
            sub_branches = branch[1]
            if sub_branches == []:
                number_totals[num] = 1
                continue
            else:
                for b in sub_branches:
                    subtotal += number_totals[b]
            number_totals[num] = subtotal
    print(number_totals[0])
