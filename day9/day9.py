#!python3
import collections
from helpers.read_lines import *
from typing import List
input = read_line_input("day9")

#sample input
# input = [
#     "35",
#     "20",
#     "15",
#     "25",
#     "47",
#     "40",
#     "62",
#     "55",
#     "65",
#     "95",
#     "102",
#     "117",
#     "150",
#     "182",
#     "127",
#     "219",
#     "299",
#     "277",
#     "309",
#     "576"
# ]

def parse_input() -> List:
    numbers = []    
    for line in input:
        numbers.append(int(line.strip()))
    return numbers

def check_cipher(queue:List, number:int) -> bool:
    for num in queue:
        if num == number:
            continue
        if abs(number-num) in queue:
            return True
    return False

def build_queue(ql:int) -> List:
    queue = collections.deque()
    all_numbers = parse_input()
    for i in range(ql):
        queue.append(all_numbers[i])
    numbers = all_numbers[ql:]
    return queue, numbers

def p1():
    queue, numbers = build_queue(25)
    for number in numbers:
        if not check_cipher(queue, number):
            print(f"check_cipher failed on: {number}")
            break
        queue.popleft()
        queue.append(number)


def p2():
    numbers = parse_input()
    target = 27911108
    pos = 0
    while pos < len(numbers):
        queue = collections.deque()
        q_pos = pos
        while sum(queue) < target:
            queue.append(numbers[q_pos])
            q_pos += 1
        if sum(queue) == target:
            print("continous block found")
            print(f"min: {min(queue)}, max {max(queue)}")
            print(f"sum of those {min(queue)+max(queue)}")
            print(f"The list was {len(queue)} numbers long")
            break
        pos += 1

def run():
    p1()
    p2()
    



    


