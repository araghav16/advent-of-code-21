#https://adventofcode.com/2021/day/11

import os, sys
import numpy as np

def getInput():
    oct_energy_lvl = np.zeros(shape=(10,10),dtype=int)
    line_list = []

    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            line = list(line.strip())
            line = list(map(int, line))
            line_list.append(line)

    #Stack arrays in sequence vertically (row wise).
    oct_energy_lvl = np.vstack(line_list)

    return oct_energy_lvl


def checkAndUpdateNeighbours(ix,iy,octopus_affected):
    #Get neighbours
    #(-1,-1) (-1,0) (-1,1)
    #(0,-1) (0,0) (0,1)
    #(1,-1) (1,0) (1,1)
    for x,y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        adj_x = ix + x
        adj_y = iy + y

        #Bail if index not within boundary
        if not ((0 <= adj_x and adj_x < 10) and (0 <= adj_y and adj_y < 10)):
            continue
        
        octopus_affected[adj_x,adj_y] += 1 #Increment adj Octopus

#PART 1
def part1_2(octopuses):
    steps = 500
    total_flashes = 0

    for step in range(1,steps+1):
        #Track octopuses that have flashed
        flashed_octopus = np.zeros(shape=(10,10), dtype=bool)

        for ix, iy in np.ndindex(octopuses.shape):
            octopuses[ix,iy] += 1

        check_for_updates = True 

        while check_for_updates:
            check_for_updates = False
            octopus_affected = np.zeros((10,10), dtype=int)

            for ix, iy in np.ndindex(octopuses.shape):
                if not flashed_octopus[ix,iy] and octopuses[ix,iy] > 9: #If hasn't flashed and is ready
                    total_flashes += 1
                    flashed_octopus[ix,iy] = True
                    check_for_updates = True

                    checkAndUpdateNeighbours(ix,iy,octopus_affected)
            
            octopuses += octopus_affected

        #Reset octopuses that have flashed
        flashed_octopus_count = 0
        for ix, iy in np.ndindex(octopuses.shape):
            if flashed_octopus[ix,iy]:
                octopuses[ix,iy] = 0
                flashed_octopus_count += 1

        if flashed_octopus_count == 100:
            print("All octopuses flash simultaneously at step {0}".format(step))

        # print("Step: {0} Total Flashes {1}\n {2}".format(step,total_flashes,octopuses))

    return total_flashes

if __name__ == "__main__":
    octopuses = getInput()
    print(octopuses )
    
    #Part 1

    total_flashes = part1_2(octopuses )
    print("Part 1: {0}".format(total_flashes))