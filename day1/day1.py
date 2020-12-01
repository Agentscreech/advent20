#!python3
from helpers.read_lines import *
from typing import List
numbers = read_line_input("day1")

#find the 2 numbers in the list that add to 2020

#one loop that points at the first number, iterating
#inner loop that does goes from len()-1 and checks the sum of the 2
#print the product of those two

def return_product(num1:int, num2:int) -> int:
    return num1 * num2

def check_for_2020(num1:int, num2:int) -> bool:
    if num1 + num2 == 2020:
        return True
    else:
        return False

def inner_loop(num1:int, arr:List[str]) -> bool:
    for num2 in arr:
        if check_for_2020(num1, int(num2)):
            return return_product(num1, int(num2))
    return False


def run():
    for i in range(len(numbers)):
        answer = inner_loop(int(numbers[i]), numbers[i:])
        if not answer:
            continue
        print(answer)
