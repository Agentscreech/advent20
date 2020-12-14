#!python3
import copy
from itertools import product
from helpers.read_lines import *
from typing import List, Tuple
input = read_line_input("day14")

sample1 = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0",
]

sample2 = [
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1",
]

#f"{num:36b}" == string in binary with zero file to 36 bit
#int("b", 2) goes back to dec
def p1():
    mem = {}
    mask = ""
    addr = 0
    bits = ""
    for line in input:
        line = line.strip()
        if "mask" in line:
            mask = line.split(" ")[2]
            continue
        else:
            addr = int(line.split(" ")[0][4:-1])
            bits = list(f'{int(line.split(" ")[2]):036b}')
        for i in range(len(mask)):
            if mask[i] == "1":
                bits[i] = "1"
            if mask[i] == "0":
                bits[i] = "0"
        mem[addr] = "".join(bits)

    total = 0
    for num in mem:
        total += int(mem[num], 2)
    print(total)


#map(list, product([0, 1], repeat=(len(of Xes))))

def run():
    mem = {}
    mask = ""
    addr = 0
    bits = ""
    for line in input:
        qty_x = 0
        loc_x = []
        line = line.strip()
        if "mask" in line:
            mask = line.split(" ")[2]
            continue
        else:
            addr = list(f'{int(line.split(" ")[0][4:-1]):036b}')
            bits = int(line.split(" ")[2])
        for i in range(len(mask)):
            if mask[i] == "X":
                addr[i] = "X"
                qty_x += 1
                loc_x.append(i)
                continue
            if mask[i] == "1":
                addr[i] = "1"
        #make floating addr
        possibilites = map(list, product([0, 1], repeat=qty_x)) 
        for poss in possibilites:
            for i in range(len(poss)):
                addr[loc_x[i]] = str(poss[i])
            mem[int("".join(addr),2)] = bits
    
    total = 0
    for num in mem:
        total += mem[num]
    print(total)

    

                
