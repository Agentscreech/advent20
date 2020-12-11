#!python3
import copy 
from helpers.read_lines import *
from typing import List, Tuple
input = read_line_input("day11")


sample1 = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL"
]

def parse_input(input:List) -> List:
    grid = []
    for line in input:
        grid.append(list(line.strip()))
    return grid

def check_ajacent(seat:Tuple,grid) -> int:
    occupied = 0 
    x_max = len(grid)-1
    y_max = len(grid[0])-1       
    x = seat[0]
    y = seat[1]
    if x-1 >= 0 and y-1 >= 0:
        if up_left(x,y,grid):
            occupied += 1
    if x-1 >= 0:
        if up(x,y,grid):
            occupied += 1
    if y-1 >= 0:
        if left(x,y,grid):
            occupied += 1
    if y+1 <= y_max:
        if right(x,y,grid):
            occupied += 1 
    if x-1 >= 0 and y+1 <= y_max:     
        if up_right(x,y,grid):
            occupied += 1
    if x+1 <= x_max:
        if down(x,y,grid):
            occupied += 1
    if y-1 >= 0 and x < x_max:
        if down_left(x,y,grid):
            occupied += 1
    if y+1 <= y_max and x < x_max:
        if down_right(x,y,grid):
            occupied += 1
    return occupied
            
def up_left(x:int, y:int, grid:List) -> bool:
    #-x -y
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False

def up(x:int, y:int, grid:List) -> bool:
    #-x y
    while x > 0:
        x -=1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False

def up_right(x:int, y:int, grid:List) -> bool:
    #-x +y
    while x > 0 and y < len(grid[0])-1:
        x -= 1
        y += 1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False

def left(x:int, y:int, grid:List) -> bool:
    #x -y
    while y > 0:
        y -= 1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False

def right(x:int, y:int, grid:List) -> bool:
    #x +y
    while y < len(grid[0])-1:
        y += 1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False

def down_left(x:int, y:int, grid:List) -> bool:
    #+x, -y
    while x < len(grid)-1 and y > 0:
        x += 1
        y -= 1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False


def down(x:int, y:int, grid:List) -> bool:
    #+x y
    while x < len(grid)-1:
        x += 1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False

def down_right(x:int, y:int, grid:List) -> bool:
    #+x +y
    while x < len(grid)-1 and y < len(grid[0])-1:
        x += 1
        y += 1
        if grid[x][y] == "#":
            return True
        if grid[x][y] == "L":
            return False
    return False

def check_grids(grid:List, new_grid:List) -> bool:
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != new_grid[x][y]:
                return False
    return True

def count_occupied(grid:List) -> int:
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "#":
                total += 1
    return total

def run():
    grid = parse_input(input)
    new_grid = copy.deepcopy(grid)
    while True:
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == ".":
                    continue
                occupied = check_ajacent((x, y), grid)
                if occupied == 0:
                    new_grid[x][y] = "#"
                if occupied >= 5:
                    new_grid[x][y] = "L"
        if not check_grids(grid, new_grid):
            grid = copy.deepcopy(new_grid)
        else:
            print(count_occupied(grid))
            break


