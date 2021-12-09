#https://adventofcode.com/2021/day/9

import os, sys
import numpy as np

def getInput():
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        hmap = []
        for line in file_in:
            #ToDo: Refine
            tmp = line.strip()
            row = []
            for digit in tmp:
                row.append(int(digit))

            hmap.append(row)

    heightmap = np.array(hmap)
    return heightmap

#PART 1
def getAdjacentValues(heightmap,x,y):
    values = []
    if y == 0:
        left = np.nan
        right = heightmap[x,y+1]
    elif y == (len(heightmap[0])-1):
        right = np.nan
        left = heightmap[x,y-1]
    else:
        right = heightmap[x,y+1]
        left = heightmap[x,y-1]

    if x == 0:
        up = np.nan
        bottom = heightmap[x+1,y]
    elif x == (len(heightmap)-1):
        bottom = np.nan
        up = heightmap[x-1,y]
    else:
        up = heightmap[x-1,y]
        bottom = heightmap[x+1,y]

    values += left,right,up,bottom
    return values

def isMinComparedToAdjacent(value, adjacentValues):
    minval = int(np.nanmin(adjacentValues))
    if value < minval:
        return True
    return False

def findMinValue(heightmap):
    low_points = []
    rows = len(heightmap)
    columns = len(heightmap[0])
    for x in range (0, rows):
        for y in range(0, columns):
            values = getAdjacentValues(heightmap,x,y)
            if isMinComparedToAdjacent(heightmap[x,y], values):
                low_points.append(heightmap[x,y])
                print("{0} values: {1}".format(heightmap[x,y], values))

    print(low_points)
    return low_points

def calculateRiskLevel(low_points):
    result = 0
    for p in low_points:
        result += p+1

    return result

#PART 2
def getLowValues(heightmap):
    low_points = []
    rows = len(heightmap)
    columns = len(heightmap[0])
    for x in range(rows):
        for y in range(columns):
            is_low = True
            for direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]: #right,left,up,down
                x_axis = x + direction[0]
                y_axis = y + direction[1]

                #Bail if index not within boundary
                if not ((0 <= x_axis and x_axis < rows) and (0 <= y_axis and y_axis < columns)):
                    continue

                if heightmap[x_axis][y_axis] <= heightmap[x][y]:
                    is_low = False
                    break

            if is_low:
                low_points.append((x, y))

    return low_points

def findBasins(heightmap, low_points):
    rows = len(heightmap)
    columns = len(heightmap[0])

    candidate_matrix = np.zeros((rows, columns), dtype=int)
    basin_count = 1
    
    for x,y in low_points:
        candidates = [(x,y)]
        considered = []

        while len(candidates) > 0:
            # print("Considering {0},{1}".format(x,y))
            x,y = candidates.pop()

            if (x,y) in considered:
                continue
            considered.append((x,y))

            #Mark all index considered with the basin count
            candidate_matrix[x,y] = basin_count

            for direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]: #right,left,up,down
                x_axis = x + direction[0]
                y_axis = y + direction[1]

                if not ((0 <= x_axis and x_axis < rows) and (0 <= y_axis and y_axis < columns)):
                    #Bail if index not within boundary
                    continue
                elif heightmap[x_axis,y_axis] == 9:
                    continue
                elif heightmap[x_axis,y_axis] > heightmap[x,y]:
                    candidates.append((x_axis,y_axis))
        else:
            basin_count += 1

    return candidate_matrix

def getBasinSize(candidate_matrix):
    #Flatten the 2d array
    flatten_basins = candidate_matrix.flatten()
    basin_sizes = np.bincount(flatten_basins)
    basin_sizes[0] = 0 #Reset basin size for 0
    basin_sizes.sort()

    #Top 3 sizes
    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]

if __name__ == "__main__":
    heightmap = getInput()
    print(heightmap)
    
    # low_points = findMinValue(heightmap)
    # part1 = calculateRiskLevel(low_points) 
    # print("Part 1: {0}".format(part1))

    low_points = getLowValues(heightmap)
    candidate_matrix= findBasins(heightmap, low_points)
    result = getBasinSize(candidate_matrix)
    print("Part 2: {0}".format(result))
