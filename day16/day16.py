#!python3
import copy
from collections import deque
from os import remove
from helpers.read_lines import *
from typing import List, Tuple, Dict
input = read_line_input("day16")

def parse_input(input):
    output = {}
    rules = {}
    mine = []
    nearby = []
    section = 0
    for line in input:
        if line == "\n":
            section += 1
            continue
        line = line.strip()
        if section == 0:
            rule = []
            sub = line.split(": ")
            s_nums = sub[1].split(" or ")
            for r in s_nums:
                rule.append(r.split("-"))
            rules[sub[0]] = rule
            continue
        if section == 1:
            if "your ticket:" in line:
                continue
            for n in line.split(","):
                mine.append(int(n))
            continue
        if section == 2:
            if "nearby tickets:" in line:
                continue
            t = []
            for n in line.split(","):
                t.append(int(n))
            nearby.append(t)
    output["rules"] = rules
    output["mine"] = mine
    output["nearby"] = nearby
    return output

sample1 = [
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "\n",
    "your ticket:",
    "7, 1, 14",
    "\n",
    "nearby tickets:",
    "7, 3, 47",
    "40, 4, 50",
    "55, 2, 20",
    "38, 6, 12"
]

sample2 = [
    "class: 0-1 or 4-19",
    "row: 0-5 or 8-19",
    "seat: 0-13 or 16-19",
    "\n",
    "your ticket:",
    "11, 12, 13",
    "\n",
    "nearby tickets:",
    "3, 9, 18",
    "15, 1, 5",
    "5, 14, 9"
]

def p1():
    output = parse_input(sample2)
    valid = []
    for rule in output["rules"]:
        for r in output["rules"][rule]:
            for i in range(int(r[0]), int(r[1])+1):
                if i not in valid:
                    valid.append(i)
    total = 0
    for t in output["nearby"]:
        for num in t:
            if num not in valid:
                total += num
    print(total)

def check_tickets(o_tickets:List, valid:List) -> List:
    tickets = copy.deepcopy(o_tickets)
    for t in tickets:
        for num in t:
            if num not in valid:
                # print(f"removing: {t}")
                o_tickets.remove(t)
                break
    return o_tickets

def remove_existing(rule:str, previous:List, index_list:Dict):
    p = copy.deepcopy(previous)
    for i, l in enumerate(p):
        if rule in l and len(previous[i]) > 1:
            previous[i].remove(rule)
            if len(previous[i]) == 1:
                index_list[previous[i][0]] = i
                previous, index_list = remove_existing(previous[i][0], previous, index_list)
    return previous, index_list

def p2():
    output = parse_input(input)
    #remove the invalid tickets
    valid = []
    for rule in output["rules"]:
        for r in output["rules"][rule]:
            for i in range(int(r[0]), int(r[1])+1):
                if i not in valid:
                    valid.append(i)
    output["nearby"] = check_tickets(output["nearby"], valid)
    #find possible places
    places = []
    index_list = {}
    for i in range(len(output["mine"])):
        possible = []
        not_poss = []
        for k in index_list.keys():
            not_poss.append(k)
        for t in output["nearby"]:
            for rule in output["rules"]:
                if rule in not_poss:
                    continue
                poss = False
                for s in output["rules"][rule]:
                    if t[i] in range(int(s[0]), int(s[1])+1):
                        poss = True
                if poss:
                    if rule not in possible and rule not in not_poss:
                        possible.append(rule)
                else:
                    if rule not in not_poss:
                        not_poss.append(rule)
                    if rule in possible:
                        possible.remove(rule)
        if len(possible) == 1:
            index_list[possible[0]] = i
        places.append(possible)

    #use recursion to remove the places from each index that we know are not it
    #start with the ones that have 1 possiblity
    f = list(index_list.keys())
    while len(index_list.keys()) < len(output["mine"]):
        for k in f:
            places, index_list = remove_existing(k, places, index_list)
    
    #now multiply all the values in the index of my ticket that have "departure" in them
    total = 1
    for i in index_list:
        if "departure" in i:
            total *= output["mine"][index_list[i]]
    print(total)
