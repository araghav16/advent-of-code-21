#https://adventofcode.com/2021/day/2
import os, sys

def getInput():
    input = {}
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            key = line.split()[0]
            value = int(line.split()[1])
            try:
                input[key].append(value)
            except KeyError:
                input[key] = [value]

    return input

def calculate_course(input):
    horizontal_pos = sum(input['forward'])

    down = sum(input['down'])
    up = sum(input['up'])
    depth = down - up

    print("Horz Pos: {0} \n\
          Down: {1} \n\
          Up: {2} \n \
          Depth: {3}".format(horizontal_pos,down,up,depth))

    return horizontal_pos*depth


if __name__ == "__main__":
    input = getInput()

    #Part 1
    result = calculate_course(input)
    print("Final location: {0}".format(result))
