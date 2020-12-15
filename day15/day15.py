#!python3
import copy
from collections import deque
from helpers.read_lines import *
from typing import List, Tuple
input = read_line_input("day15")


def parse_data(input):
    output = []
    for line in input:
        line = line.strip()
        return line.split(",")


sample1 = [
    "0, 3, 6"
]

def p1():
    output = parse_data(input)
    turn = 0
    nums = {}
    spoken = 0
    #keep track of how many turns it's been since the last time the number was "spoken"
    #use a queue of len 2 for each spoken number
    #keep track of if the number was spoken at all
    #if not spoken, next is 0
    for num in output:
        turn += 1
        spoken = int(num)
        nums[spoken] = deque()
        nums[spoken].append(0)
        nums[spoken].append(turn)
    turn += 1
    spoken = 0
    nums[spoken].popleft()
    nums[spoken].append(turn)
    spoken = nums[spoken][1] - nums[spoken][0]
    turn += 1
    #part 1 is just to 2020
    while turn < 30000000:
        if spoken in nums:
            nums[spoken].popleft()
            nums[spoken].append(turn)
            spoken = nums[spoken][1] - nums[spoken][0]
        else:
            nums[spoken] = deque()
            nums[spoken].append(0)
            nums[spoken].append(turn)
            spoken = 0
        turn += 1
    print(spoken)
