#https://adventofcode.com/2021/day/7

import os, sys

def getInput():
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            horz_pos = list(map(int,(line.strip().split(','))))

    return horz_pos


def createPositionSummary(horz_pos):
    #Create a dict of occurrences count for each Horz position
    pos_dict = {}
    for pos in horz_pos:
        if pos not in pos_dict:
            pos_dict[pos] = horz_pos.count(pos)

    return pos_dict

def calculateMinFuelCostPart1(pos_dict):
    '''
        e.g 1 - 37 fuel
        {16: 1, 1: 2, 2: 3, 0: 1, 4: 1, 7: 1, 14: 1}
    '''
    total_fuel = []

    for key, value in pos_dict.items():
        align_horz_post = key
        fuel_cost = 0
        for key, value in pos_dict.items():
            for i in range(1,value+1):
                pos_diff = abs(key-align_horz_post)
                fuel_cost += pos_diff

        total_fuel.append(fuel_cost)

    print("Total Fuel Cost: {0}".format(total_fuel))
    min_fuel = min(total_fuel)
    return min_fuel

def calculateMinFuelCostPart2(pos_dict):
    '''
        e.g 5 - 168 fuel
        {16: 1, 1: 2, 2: 3, 0: 1, 4: 1, 7: 1, 14: 1}
    '''
    total_fuel = []
    max_pos = max(pos_dict.keys())
    min_pos = min(pos_dict.keys())

    for align_horz_pos in range(min_pos,max_pos): #For each value from min to max position
        total_fuel_for_pos = []

        for key, value in pos_dict.items(): #Calculate for each current crab Horz Position
            fuel_cost = 0
            pos_diff = abs(key-align_horz_pos)

            for _ in range(value): #For each Crab
                # Calculate fuel cost   #ToDo - Better way?
                for change_count in range(1,pos_diff+1):
                    fuel_cost += change_count

                print("Move from {0} to {1} pos_diff:{2}".format(key,align_horz_pos, pos_diff))

            total_fuel_for_pos.append(fuel_cost)
        
        print("Total Fuel Cost For Moving To {0}: {0}".format(align_horz_pos, total_fuel_for_pos))
        total_fuel.append(sum(total_fuel_for_pos))

    print("Total Fuel Cost: {0}".format(total_fuel))

    min_fuel = min(total_fuel)
    return min_fuel

if __name__ == "__main__":
    horz_pos = getInput()
    # print(horz_pos)

    pos_dict = createPositionSummary(horz_pos)
    print(pos_dict)

    # min_fuel = calculateMinFuelCostPart1(pos_dict)
    # print("Part 1: {1}".format(min_fuel))

    min_fuel = calculateMinFuelCostPart2(pos_dict)
    print("Part 2: {0}".format(min_fuel))









