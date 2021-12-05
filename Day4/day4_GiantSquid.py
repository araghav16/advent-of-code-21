#https://adventofcode.com/2021/day/4
#https://adventofcode.com/2021/day/4#part2

import os, sys
import numpy as np

def getInput():
    bingo_input = []
    bingo_boards = []
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            if ',' in line:
                tmp = line.strip().split(',')
                bingo_input = list(map(int, tmp))
            else:
                #ToDo: Refine
                tmp = line.strip().split(',')
                tmp2 = tmp[0].split(' ')
                
                while '' in tmp2:
                    tmp2.remove('')
                tmp3 = list(map(int, tmp2))
                if tmp3:
                    bingo_boards.append(tmp3)
    return bingo_input, bingo_boards 

def bingo(bingo_boards, bingo_input):
    board = np.array(bingo_boards) #Create 2d Array
    board_turns = []
    board_no = 0
    for n in range(0,len(board),5):
    # n = 265
        print("Board Number: {0} n: {1}".format(board_no, n))
        single_board = board[n:n+5]
        print(single_board)
        board_turns.append(checkMatch(single_board, bingo_input))
        board_no+=1

    winning_board = board_turns.index(min(board_turns))
    losing_board =  board_turns.index(max(board_turns))

    return(board_turns, winning_board, losing_board)

def findOccurrence(occurrence_count, item, index):
    if 0 == item[index]:
        occurrence_count[0] += 1
    elif 1 == item[index]:
        occurrence_count[1] += 1
    elif 2 == item[index]:
        occurrence_count[2] += 1
    elif 3 == item[index]:
        occurrence_count[3] += 1
    elif 4 == item[index]:
        occurrence_count[4] += 1
    elif 4 == item[index]:
        occurrence_count[5] += 1

def checkMatch(board, input):
    occurrence_count_x = [0,0,0,0,0]
    occurrence_count_y = [0,0,0,0,0]

    input_count = 0

    for number in input:
        location = np.argwhere(board == number)
        location = location.tolist()
        if len(location):
            print("Found {0} at {1}".format(number,location[0]))
        input_count+=1

        for item in location:
            findOccurrence(occurrence_count_x, item, 0)
            findOccurrence(occurrence_count_y, item, 1)

        if 5 in occurrence_count_x:
            print("Found Match X! Count:{0}, Took {1} turns at Number {2}".format(occurrence_count_x, input_count, number))
            break
        if 5 in occurrence_count_y:
            print("Found Match Y! Count:{0},Took {1} turns at Number {2}".format(occurrence_count_y, input_count, number))
            break
    
    return input_count

if __name__ == "__main__":
    bingo_input, bingo_boards = getInput()

    #Part 1 & 2
    board_turns, winning_board, losing_board = bingo(bingo_boards, bingo_input)
    print("board_turns {0}\nwinning_board id: {1}\nlosing_board id: {2}".format(board_turns, winning_board, losing_board ))

    # calculateScore()



