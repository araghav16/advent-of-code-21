#https://adventofcode.com/2021/day/14

import os, sys, collections
import numpy as np

def getInput():
    rules = {}
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            if not "->" in line:
                if line.strip():
                    template = list(line.strip())
            else:
                rule = line.strip().split('->')
                rules[rule[0].strip()]=rule[1].strip()

    return template,rules

def part1(template,rules):
    steps = 10
    updated_template = template
    for s in range(1,steps+1):
        char_stack = []
        for char in updated_template: #NNCB 
            char_stack.append(char)

            if len(char_stack) == 1:
                continue

            #Take last 2 char in char_stack
            pattern = char_stack[-2] + char_stack[-1]
            # print(pattern)

            if pattern in rules:
                # print(pattern, '->', rules[pattern])
                tmp = char_stack.pop()
                char_stack.append(rules[pattern])
                char_stack.append(tmp)

        print("After step {0}: {1}".format(s,''.join(char_stack)))
        updated_template = char_stack

    return calculateScore(updated_template)

def calculateScore(updated_template):
    occurrences = collections.Counter(updated_template)
    list_by_occurrence = occurrences.most_common()
    result = list_by_occurrence[0][1] - list_by_occurrence[-1][1]
    return result

if __name__ == "__main__":
    template,rules = getInput()
    print(template,rules)

    result = part1(template,rules)
    print("Part 1: {0}".format(result))