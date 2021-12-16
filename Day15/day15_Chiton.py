#https://adventofcode.com/2021/day/15

import os, sys, heapq
import numpy as np
from collections import defaultdict

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

    map = np.array(hmap)
    return map

def part1(map):
    map_height = map.shape[0]
    map_width = map.shape[1]
    cost_dict = defaultdict(int)

    priority_queue = [(0,0,0)] #cost, row, col
    heapq.heapify(priority_queue)
    visited = set()

    while len(priority_queue) > 0:
        cost, ix, iy = heapq.heappop(priority_queue) #Pop smallest item of heap

        if (ix,iy) in visited:
            continue
        visited.add((ix,iy))

        cost_dict[(ix,iy)] = cost

        if ix == map_height-1 and iy == map_width-1:
            print("Reached end {0},{1}".format(ix,iy))
            break

        #Push in queue cost of adj values
        for dx,dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: #[(0, 1),(1, 0)]: #
            xx = ix + dx
            yy = iy + dy
            #Check within grid
            if not (0 <= xx < map_height and 0 <= yy < map_width):
                continue

            heapq.heappush(priority_queue, (cost + map[xx][yy], xx,yy))

    return cost_dict[(map_height - 1, map_width - 1)]

if __name__ == "__main__":
    map  = getInput()
    print(map)

    result = part1(map)
    print("Part 1: {0}".format(result))
