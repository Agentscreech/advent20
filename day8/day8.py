#!python3
from day4.day4 import parse_entries
from helpers.read_lines import *
from typing import List
import copy
input = read_line_input("day8")


def parse_input():  
    instruction_list = []
    for line in input:
        temp = line.split(" ")
        instruction_list.append((temp[0], int(temp[1].strip())))
    return instruction_list


#sample:
# input = [
#     "nop +0",
#     "acc +1",
#     "jmp +4",
#     "acc +3",
#     "jmp -3",
#     "acc -99",
#     "acc +1",
#     "jmp -4",
#     "acc +6",
# ]

def p1(instruction_list):
    acc = 0
    position = 0
    used_ins = [0] * len(instruction_list)
    while True:
        if used_ins[position] == 1:
            print(f"Already did that instruction: {acc}")
            break
        ins = instruction_list[position][0]
        val = instruction_list[position][1]
        if ins == "nop":
            used_ins[position] = 1
            position += 1
            continue
        if ins == "acc":
            used_ins[position] = 1
            acc += val
            position += 1
            continue
        if ins == "jmp":
            used_ins[position] = 1
            position += val
            continue

def find_ins(target:str, instruction_list:List) -> List:
    ins_pos = []
    for i, ins in enumerate(instruction_list):
        if ins[0] == target:
            ins_pos.append(i)
    return ins_pos


def check_infinite(instruction_list):
    acc = 0
    position = 0
    used_ins = [0] * len(instruction_list)

    while position < len(used_ins):
        if used_ins[position] == 1:
            return True
        ins = instruction_list[position][0]
        val = instruction_list[position][1]
        if ins == "nop":
            used_ins[position] = 1
            position += 1
            continue
        if ins == "acc":
            used_ins[position] = 1
            acc += val
            position += 1
            continue
        if ins == "jmp":
            used_ins[position] = 1
            position += val
            continue
    print(acc)
    return False

def p2(instruction_list):
    nops = find_ins("nop", instruction_list)
    jmps = find_ins("jmp", instruction_list)
    #swap jmp for nop
    for jmp in jmps:
        temp_list = copy.deepcopy(instruction_list)
        val = temp_list[jmp][1]
        temp_list[jmp] = ("nop", val)
        is_inf = check_infinite(temp_list)
        if not is_inf:
            print("Didn't loop, Done")
            break

def run():
    instruction_list = parse_input()
    p1(instruction_list)
    p2(instruction_list)
