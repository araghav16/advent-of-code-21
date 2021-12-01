#https://adventofcode.com/2021/day/1
import os, sys

def getInput():
    input = []
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            input.append(int(line.strip()))        
    return input

def detectDepthIncrease(input):
    prev_value = input[0]
    depth_increase_count = 0
    for value in input[1:]:
        if prev_value < value:
            depth_increase_count += 1
            print("Increased: Prev Value: {0}, Value: {1} depth_increase_count: {2}".format(prev_value, value, depth_increase_count))
        else:
            print("Unchanged: Prev Value: {0}, Value: {1} depth_increase_count: {2}".format(prev_value, value, depth_increase_count))

        prev_value = value

    return depth_increase_count

if __name__ == "__main__":
    input = getInput()
    result = detectDepthIncrease(input)
    print("Depth Measurement Increases: {0} times".format(result))

