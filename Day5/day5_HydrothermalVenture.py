#https://adventofcode.com/2021/day/5
#https://adventofcode.com/2021/day/5#part2

import os, sys
import numpy as np

def getInput():
    vent_lines_input = []
    max_x = max_y = 0
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            line_seg = 0
            tmp = line.strip().split('->')

            line_seg = (tmp[0].strip(), tmp[1].strip())
            max_x, max_y = getMaxGrid(line_seg, max_x, max_y)

            vent_lines_input.append(line_seg)

    return vent_lines_input, max_x, max_y

def getMaxGrid(line_seg, max_x, max_y):
    for entry in line_seg:
        tmp = entry.split(',')
        x = int(tmp[0])
        y = int(tmp[1])
        if x > max_x:
            max_x = x
            # print("Max X Updated: {0}".format(max_x))
        if y > max_y:
            max_y = y
            # print("Max Y Updated: {0}".format(max_y))
            
    # print("Max X: {0}, Max Y: {1}".format(max_x,max_y))
    return max_x,max_y

def markVentsOnGrid(grid, cord1, cord2):
    print(cord1,cord2)
    #Are we going along X or Y
    horizontal_vent = vertical_vent = False
    np.set_printoptions(threshold=sys.maxsize)

    if cord1[0] == cord2[0]:
        print("Vertical!")
        min_cord = min([cord1[1],cord2[1]])
        max_cord = max([cord1[1],cord2[1]])
        print("Min Cord {0}, Max Cord {1}".format(min_cord,max_cord))
        for i in range(min_cord,max_cord+1):
            # print("Updating Cord: {0},{1}".format(i, cord1[0]))
            grid[i, cord1[0]] +=1
    elif cord1[1] == cord2[1]:
        print("horizontal!")
        min_cord = min([cord1[0],cord2[0]])
        max_cord = max([cord1[0],cord2[0]])
        print("Min Cord {0}, Max Cord {1}".format(min_cord,max_cord))
        for i in range(min_cord,max_cord+1):
            # print("Updating Cord: {0},{1}".format(cord1[1],i))
            grid[cord1[1],i] +=1
    else: 
        # print("Diagonal skipping!") #Part 1
        print("Diagonal!")
        direction = [dir(cord2[0] - cord1[0]), dir(cord2[1] - cord1[1])]
        print("Direction {0}".format(direction))

        # To Do: Condense this further?
        if (direction[0],direction[1]) == (1,1) or (direction[0],direction[1]) == (-1,-1): # e.g 6,4 -> 2,0 | 0,0 -> 8,8
            update_x, update_y = cord1[0],cord1[1]
            while not (update_x,update_y) == cord2:
                print("Update Cord: {0},{1}".format(update_x,update_y))
                grid[update_y,update_x] +=1
                update_x += direction[1]
                update_y += direction[0]
            print("Update Cord End: {0},{1}".format(update_x,update_y))
            grid[update_y,update_x] +=1
        elif (direction[0],direction[1]) == (-1,1) or (direction[0],direction[1]) == (1,-1): #e.g 5,5 -> 8,2 or  8,0 -> 0,8
            update_x, update_y = cord2[0],cord2[1]
            while not (update_x,update_y) == cord1:
                print("Update Cord: {0},{1}".format(update_x,update_y))
                grid[update_y,update_x] +=1
                update_x += direction[1]
                update_y += direction[0]
            print("Update Cord End: {0},{1}".format(update_x,update_y))
            grid[update_y,update_x] +=1

    # print(grid)
    return grid

def dir(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def calculateVentLines(grid, vent_lines_input):
    for value in vent_lines_input:
        cord1 = value[0].split(',')
        x1,y1 = int(cord1[0]), int(cord1[1])
        
        cord2 = value[1].split(',')
        x2,y2 = int(cord2[0]), int(cord2[1])

        cord1 = (x1,y1) 
        cord2 = (x2,y2)

        grid = markVentsOnGrid(grid, cord1, cord2)
    
    danger_area = (grid > 1).sum()
        
    return danger_area

if __name__ == "__main__":
    vent_lines_input, max_x, max_y = getInput()
    # print(vent_lines_input)

    #Create a grid max_x * max_y filled with 0s
    print("Size: max_x:{0},max_y:{1}".format(max_x+3,max_y+1))
    grid = np.zeros(shape=(max_x+3,max_y+1), dtype=int) #ToDo Debug +3

    #Part 1
    danger_area = calculateVentLines(grid, vent_lines_input)
    print("Danger Area (>1): {0}".format(danger_area))



