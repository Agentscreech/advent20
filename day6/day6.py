#!python3
from helpers.read_lines import *
from typing import List
input = read_line_input("day6")


#pt1
def run_p1():
    count = 0
    group_yes = ""
    for line in input:
        if line == "\n":
            count += len(set(group_yes))
            group_yes = ""
        else:
            group_yes += line.strip()
    print(count)


#pt
def run_p2():
    count = 0
    group_yes = ""
    for line in input:
        if line == "\n":
            count += len(group_yes)
            group_yes = ""
        elif group_yes == "":
            group_yes = set(line.strip())
        else:
            group_yes = set(group_yes).intersection(line.strip())
    print(count)
            
