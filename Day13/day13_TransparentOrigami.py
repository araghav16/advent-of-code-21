#https://adventofcode.com/2021/day/12

import os, sys
import numpy as np

# The first value, x, increases to the right. 
# The second value, y, increases downward

def getInput(size):
    dots = []
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            if "," in line:
                line = line.strip().split(',')
                x = int(line[0])
                y = int(line[1])

            dots.append((x,y))

    dots_grid = np.zeros(shape=(size[1],size[0]),dtype=int)
    # print(dots_grid)

    #Fill grid
    for dot in dots:
        dots_grid[dot[1],dot[0]] = 1

    return dots_grid

def fold(dots_grid, fold_along):
    # print(dots_grid.shape)
    if fold_along[0] == 'y':
        folded_dots_grid = np.zeros(shape=(fold_along[1],dots_grid.shape[1]),dtype=int)
        offset = 1
        for row in range(fold_along[1]-1,-1,-1):
            for col in range(0,dots_grid.shape[1]):
                # print("{0} = {1}".format((row,col), (fold_along[1]+offset,col)))
                folded_dots_grid[row,col] = dots_grid[fold_along[1]+offset][col]
            offset+=1

        slice = -1-fold_along[1] 
        org_dots_grid = dots_grid[:slice]
        org_dots_grid += folded_dots_grid

        return org_dots_grid
    if fold_along[0] == 'x':
        folded_dots_grid = np.zeros(shape=(dots_grid.shape[0],fold_along[1]),dtype=int)
        for row in range(0,dots_grid.shape[0]):
            offset = dots_grid.shape[1]-1 #Start from Last index
            for col in range(0,fold_along[1]):
                folded_dots_grid[row,col] = dots_grid[row][offset]
                offset-=1

        org_dots_grid = np.delete(dots_grid,np.s_[fold_along[1]:dots_grid.shape[1]],axis=1)
        # print(org_dots_grid)
        # print(folded_dots_grid)
        org_dots_grid += folded_dots_grid
        return org_dots_grid

def countDots(dots_grid):
    #Flatten the 2d array
    dots_grid = dots_grid.flatten()
    dots_count = np.bincount(dots_grid)
    return np.sum(dots_count)-dots_count[0]

def correctChar(dots_grid):
    for ix, iy in np.ndindex(dots_grid.shape):
        if not dots_grid[ix,iy] == 0:
            dots_grid[ix,iy] = 1
    return dots_grid


if __name__ == "__main__":
    size = (1311,895) #(11,15) (1311,895) #Calcualted via fold x,y
    dots_grid = getInput(size)
    print("Input: \n",dots_grid)

    #Example
    # dots_grid = fold(dots_grid, ('y',7))
    # print("After fold: \n", dots_grid)
    # dots_grid = fold(dots_grid, ('x',5))
    # print("After fold: \n", dots_grid)

    #Input 
    folds = [('x',655),('y',447),('x',327),('y',223),('x',163),('y',111),('x',81),('y',55),('x',40),('y',27),('y',13),('y',6)]

    for instruction in folds:
        dots_grid = fold(dots_grid, instruction)

    dots_grid= correctChar(dots_grid)
    print(dots_grid)

    
    # result = countDots(dots_grid)
    # print("Part 1: {0}".format(result))