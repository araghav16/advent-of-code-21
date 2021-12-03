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

def detectDepthIncreaseSlidingWindow(input):
    prevRunningSum = input[0] + input[1] + input[2]
    print(prevRunningSum)
    depth_increase_count = 0 
    for idx, value in enumerate(input[1:-1]):
        currentRunningSum = input[idx] + input[idx+1] + input[idx+2]
        print("currentRunningSum: {0}".format(currentRunningSum))
        if currentRunningSum > prevRunningSum:
            depth_increase_count+=1
            print("Increased: prevRunningSum: {0}, currentRunningSum: {1}".format(prevRunningSum, currentRunningSum))
        else:
            print("Unchanged: prevRunningSum: {0}, currentRunningSum: {1}".format(prevRunningSum, currentRunningSum))

        prevRunningSum = currentRunningSum

    return depth_increase_count

if __name__ == "__main__":
    input = getInput()
    print(input)
    #Part 1
    # result = detectDepthIncrease(input)
    # print("Depth Measurement Increases: {0} times".format(result))

    #Part 2 
    result = detectDepthIncreaseSlidingWindow(input)
    print("Depth Measurement Increases (Three Measurements Sliding Window): {0} times".format(result))

