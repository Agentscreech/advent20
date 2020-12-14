#!python3
import copy
from helpers.read_lines import *
from typing import List, Tuple
input = read_line_input("day13")


def parse_input(input):
    output = []
    output.append(int(input[0]))
    times = input[1].split(",")
    for num in times:
        num = num.strip()
        if num != "x":
            output.append(int(num))
    return output

sample1 = [
    "939",
    "7, 13, x, x, 59, x, 31, 19"
]
s2 = [
    "f",
    "17, x, 13, 19"
]

def p1():
    #divide start by each number, closest without going over, then multiply it by the quotent+1
    out = parse_input(input)
    now = out[0]
    whole = 0
    bus_id = 0
    q = 0
    for num in out[1:]:
        integer = now//num
        rem = (now/num)%1
        if rem > q:
            q = rem
            bus_id = num
            whole = integer
    next_time = bus_id * (whole + 1)
    print((next_time - now) * bus_id)

def p2():
    #this alg works, but it takes forever. Apparently you have to use something called
    #Chinese Remainder therom, which I never heard about.
    out = input[1].split(",")
    interval = int(max(out[0]))
    time = 0
    found = False
    while not found:
        if time%int(out[0]) == 0:
            seq = True
            for i, num in enumerate(out[1:]):
                i = i+1
                num = num.strip()
                if num != "x":
                    if int(num) != (time%int(num))+i:
                        seq = False
                        break
            if seq:
                found = True
        time *= num
    print(time-interval)

