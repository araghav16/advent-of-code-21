#https://adventofcode.com/2021/day/10

import os, sys
import numpy as np

def getInput():
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        nav = []
        for line in file_in:
            tmp = line.strip()
            nav.append(tmp)

    return nav

#PART 1
def isChunkValid(nav):
    valid_closures = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>',
    }

    invalid_char = []

    for entry in nav:
        char_debug_list = []
        next_valid_closure = []
        for char in entry:
            char_debug_list.append(char)

            #if char is a closure, is it == next_valid_closure
            if char in ['(','[','{','<']:
                next_valid_closure.append(valid_closures[char])

            if char in [')',']','}','>']:
                if not char == next_valid_closure[-1]:
                    # print("Found Invalid {0}, when expected {1}, Stack: {2}".format(char,next_valid_closure[-1],char_debug_list))
                    invalid_char.append(char)
                    break
                else:
                    next_valid_closure.pop()
                    
    print(invalid_char)
    return invalid_char

def calculateInvalidCharScore(invalid_char):
    illegal_char_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    total = 0
    for char in invalid_char:
        total += illegal_char_score[char]

    return total

# PART 2
def calculateAutoCompleteScore(incomplete_brackets):
    auto_complete_score = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    score = 0

    for b in reversed(incomplete_brackets):
        score = score * 5
        score += auto_complete_score[b]
        print(score)

    return score

def removeInputOfCorruption(nav):
    valid_closures = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>',
    }

    cleaned_nav = []

    for entry in nav:
        char_debug_list = []
        next_valid_closure = []
        found_invalid = False
        for char in entry:
            char_debug_list.append(char)

            if char in ['(','[','{','<']:
                next_valid_closure.append(valid_closures[char])

            #if char is a closure, is it == next_valid_closure
            if char in [')',']','}','>']:
                if not char == next_valid_closure[-1]:
                    # print("Found Invalid {0}, when expected {1}, Stack: {2}".format(char,next_valid_closure[-1],char_debug_list))
                    found_invalid = True
                    break
                else:
                    next_valid_closure.pop()

        if not found_invalid:
            cleaned_nav.append(entry)

    # print(cleaned_nav)
    return cleaned_nav

def getIncompleteChars(cleaned_nav):
    valid_closures = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>',
    }

    incomplete_lines_score = []

    for entry in cleaned_nav:
        incomplete_brackets = []
        
        for char in entry:
            if char in ['(','[','{','<']:
                incomplete_brackets.append(char)

            if char in [')',']','}','>']:
                last_bracket = incomplete_brackets.pop()
                if not valid_closures[last_bracket] == char:
                    print("Error {0} != {1}".format(last_bracket,char))
            
    

        print("{0} - Complete by adding {1}".format(entry,incomplete_brackets))
        score = calculateAutoCompleteScore(incomplete_brackets)
        incomplete_lines_score.append(score)

    incomplete_lines_score.sort()
    print(incomplete_lines_score)
    middle_index = int(len(incomplete_lines_score) / 2)

    return incomplete_lines_score[middle_index]

'''
Unnecessary func: Gives occurrence count of each bracket in a line.
'''
def getIncompleteChars_2(nav):
    incomplete_chars = []

    for entry in nav:
        char_expected = {
            '(': 0,
            ')': 0,
            '[': 0,
            ']': 0,
            '{': 0,
            '}': 0,
            '<': 0,
            '>': 0,
        }
        char_array = list(entry)
        tmp = np.array(char_array)
        brackets, count = np.unique(tmp, return_counts=True)

        brackets = brackets.tolist()
        count = count.tolist()

        for b in char_expected:
            if b in brackets:
                index = brackets.index(b)
                char_expected[b] = count[index]

        print(char_expected)
        keys_list = list(char_expected)
        for i in range(0,7,2):
            open_bracket = keys_list[i]
            close_bracket = keys_list[i+1]
            if not char_expected[open_bracket] == char_expected[close_bracket]:
                incomplete_chars.append(keys_list[i+1])

    print(incomplete_chars)
    return incomplete_chars

if __name__ == "__main__":
    nav = getInput()
    # print(nav)
    
    #Part 1
    # invalid_char = isChunkValid(nav)
    # result = calculateInvalidCharScore(invalid_char)
    # print("Part 1: {0}".format(result))

    # Part 2
    cleaned_nav = removeInputOfCorruption(nav)
    result = getIncompleteChars(cleaned_nav)
    print("Part 2: {0}".format(result))
