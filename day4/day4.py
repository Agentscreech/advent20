#!python3
from helpers.read_lines import *
from typing import List
input = read_line_input("day4")

def parse_entries(input:List) -> List:
    passports = []
    keys = []
    for line in input:
        #strip out the keys until there is just a new line
        if line == "\n":
            passports.append(keys)
            keys = []
            continue
        entries = line.split(' ')
        for entry in entries:
            keys.append(entry.split(":")[0])
    return passports

def check_passports(passports:List) -> int:
    valid_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    total = 0
    for p in passports:
        valid = True
        for field in valid_fields:
            if field not in p:
                valid = False
                break
        if valid:
            total += 1
    return total

def run():
    passports = parse_entries(input)
    print(check_passports(passports))

        

