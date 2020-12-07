#!python3
from helpers.read_lines import *
from typing import List
input = read_line_input("day7")

#Sample 1
# input  = [  "light red bags contain 1 bright white bag, 2 muted yellow bags.",
#             "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
#             "bright white bags contain 1 shiny gold bag.",
#             "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
#             "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
#             "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
#             "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
#             "faded blue bags contain no other bags.",
#             "dotted black bags contain no other bags."
#             ]

#Sample 2
# input = [
#     "shiny gold bags contain 2 dark red bags.",
#     "dark red bags contain 2 dark orange bags.",
#     "dark orange bags contain 2 dark yellow bags.",
#     "dark yellow bags contain 2 dark green bags.",
#     "dark green bags contain 2 dark blue bags.",
#     "dark blue bags contain 2 dark violet bags.",
#     "dark violet bags contain no other bags.",
# ]
bags = {}
bag_totals = {}
parsed_bags = []

def parse_bags(line:str):
    name = line.split("contain")[0].split(" ")[:2]
    name = " ".join(name)
    contains = line.split("contain")[1].strip().split(" ")
    temp = {}
    j = 0
    for i in range(len(contains)//4):
        temp[" ".join(contains[j+1:j+3])] = int(contains[j])
        j += 4
    bags[name] = temp

def find_bag(target_bag:str) -> List:
    holders = []
    for bag in bags:
        for color in bags[bag].keys():
            if color == target_bag:
                holders.append(bag)
    return holders

def contain_shiny(bag_list):
    for b in bag_list:
        if b in parsed_bags:
            continue
        out = find_bag(b)
        parsed_bags.append(b)
        contain_shiny(out)

def bag_count(bag):
    i = 0
    if len(bag) == 0:
        return 0
    for color in bag:
        if color in bag_totals:
            i += bag[color]+(bag_totals[color])
            continue
        bag_totals[color] = bag_count(bags[color])
        i += bag[color]
        i += bag_totals[color] * bag[color]
    return i

def run():
    for line in input:
        parse_bags(line.strip())
    #p1
    gold_out = find_bag("shiny gold")
    contain_shiny(gold_out)
    print(f"How many bag colors can eventually contain at least one shiny gold bag? {len(parsed_bags)}")
    #p2
    count = 0
    for bag in bags["shiny gold"]:
        bag_totals[bag] = bag_count(bags[bag])
        count += bags["shiny gold"][bag]
        count += bag_totals[bag] * bags["shiny gold"][bag]
    print(f"How many individual bags are required inside your single shiny gold bag? {count}")
    

    
