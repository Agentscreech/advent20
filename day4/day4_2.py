#!python3
from helpers.read_lines import *
from typing import List
import re
input = read_line_input("day4")


def parse_entries(input: List) -> List:
    passports = []
    keys = {}
    for line in input:
        #strip out the keys until there is just a new line
        if line == "\n":
            passports.append(keys)
            keys = {}
            continue
        entries = line.split(' ')
        for entry in entries:
            parts = entry.split(":")
            keys[parts[0]] = parts[1].strip()
    return passports

def check_pid(pid:str) -> bool:
    if len(pid) == 9:
        try:
            n = int(pid)
            return True
        except:
            return False

def check_ecl(ecl:str) -> bool:
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in valid_colors:
        return True
    return False

def check_hcl(hcl:str) -> bool:
    if re.search(r'^#(?:[0-9a-f]{3}){1,2}$', hcl):
        return True
    return False

def check_hgt(hgt: str) -> bool:
    try:
        y = int(hgt[:-2])
        if "cm" in hgt:
            if y >= 150 and y <=193:
                return True
        if "in" in hgt:
            if y >= 59 and y <= 76:
                return True
    except:
        return False

def check_eyr(eyr: str) -> bool:
    y = int(eyr)
    if y >= 2020 and y <= 2030:
        return True
    return False

def check_iyr(iyr: str) -> bool:
    y = int(iyr)
    if y >= 2010 and y <= 2020:
        return True
    return False

def check_byr(byr:str) -> bool:
    y = int(byr)
    if y >= 1920 and y <= 2002:
        return True
    return False

def check_passports(passports: List) -> int:
    valid_fields = {"byr":check_byr, "iyr":check_iyr, "eyr":check_eyr, "hgt":check_hgt, "hcl":check_hcl, "ecl":check_ecl, "pid":check_pid}
    total = 0
    for p in passports:
        valid = True
        for field in valid_fields.keys():
            if field not in p.keys():
                valid = False
                break
            else:
                if not valid_fields[field](p[field]):
                    valid = False
                    break
        if valid:
            total += 1
    return total


def run():
    passports = parse_entries(input)
    print(check_passports(passports))
