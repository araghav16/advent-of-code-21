#https://adventofcode.com/2021/day/2
#https://adventofcode.com/2021/day/2#part2

import os, sys

def getInput():
    input = {}
    with open(os.path.join(sys.path[0], "input_test1.txt")) as file_in:
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

def getInputPart2():
    input = []
    
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            entry = {}
            entry[line.split()[0]] = int(line.split()[1])
            input.append(entry)

    return input

def calculate_course_with_aim(input):
    horizontal_pos = aim = depth = 0

    for entry in input:
        if 'forward' in entry:
            fwd_value = entry['forward']
            horizontal_pos += fwd_value
            if aim == 0: 
                continue
            depth += aim * fwd_value
        elif 'down' in entry:
            aim += entry['down']
        elif 'up' in entry:
            aim -= entry['up']
        
        print("Input: {0} \n\
            Horz Pos: {1} \n\
          Aim: {2} \n \
          Depth: {3}".format(entry, horizontal_pos, aim, depth))

    return horizontal_pos*depth

if __name__ == "__main__":
    #Part 1
    # input = getInput()
    # result = calculate_course(input)
    # print("Final location: {0}".format(result))
    
    #Part 2
    input = getInputPart2()
    result = calculate_course_with_aim(input)
    print("Final location: {0}".format(result))

