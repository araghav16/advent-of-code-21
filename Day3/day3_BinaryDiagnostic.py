#https://adventofcode.com/2021/day/3
#https://adventofcode.com/2021/day/3#part3

import os, sys

def getInput():
    input = []
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            input.append(line.split('\n')[0])
    return input

def isNthBitSet(x: int, n:int):
    if x &(1 << n):
        return True
    return False

def diagnostic_pc(input):
    gamma_rate =  []
    epsilon_rate = []
    
    for i in range(11,-1,-1):
        zero_count = one_count = 0
        for entry in input:
            dec_entry = int(entry,2) #Convert to decimal
            # Check if first bit set to 1 
            if isNthBitSet(dec_entry, i):
                # print("{0}({1}), First Bit is set!".format(entry, dec_entry))
                one_count+=1
            else:
                zero_count+=1
            
        if one_count > zero_count:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            gamma_rate.append('0')
            epsilon_rate.append('1')

    print(gamma_rate)
    print(epsilon_rate)
    
    power_consumption = int(''.join(gamma_rate),2) * int(''.join(epsilon_rate),2)
    
    return power_consumption

def remove_entries(input, bit, index):
    # print("input before: {0}".format(input))
    for word in input[:]:
        if word[index] == bit:
            input.remove(word)
    # print("input after: {0}".format(input))
    return input

def diagnostic_lsr(input):
    result1 = get_rating(input.copy(), "oxygen")[0]
    oxygen_gen_rating = int(result1,2)

    print("----------------------------------------------------------")
    result2 = get_rating(input.copy(), "c02")[0]
    c02_scrubber_rating = int(result2,2)

    print("oxygen_gen_rating: {0}\nc02_scrubber_rating: {1}".format(oxygen_gen_rating, c02_scrubber_rating))
    life_support_rating = oxygen_gen_rating * c02_scrubber_rating

    return life_support_rating

def get_rating(input, rating_type):
    bit_length = len(input[0])-1
    for i in range(bit_length,-1,-1): #11
        zero_count = one_count = 0
        for entry in input:
            dec_entry = int(entry,2) #Convert to decimal
            # Check if first bit set to 1 
            if isNthBitSet(dec_entry, i):
                one_count+=1
            else:
                zero_count+=1
            
        print("One Count: {0}, Zero Count {1}".format(one_count, zero_count))
        if(rating_type == "oxygen"):
            if one_count > zero_count:
                # print("1 is common")
                input = remove_entries(input, '0', bit_length-i)
            elif one_count < zero_count:
                # print("0 is common")
                input = remove_entries(input, '1', bit_length-i)
            else:
                # print("Both equal")
                input = remove_entries(input, '0', bit_length-i)
        elif(rating_type == "c02"):
            if one_count > zero_count:
                # print("0 is least common")
                input = remove_entries(input, '1', bit_length-i)
            elif one_count < zero_count:
                # print("1 is least common")
                input = remove_entries(input, '0', bit_length-i)
            else:
                # print("Both equal")
                input = remove_entries(input, '1', bit_length-i)

        if(len(input) == 1):
            break

    return input

if __name__ == "__main__":
    input = getInput()
    # print(input)

    #Part 1
    # result = diagnostic_pc(input)
    # print("Power Consumption: {0}".format(result))

    #Part 2
    result = diagnostic_lsr(input)
    print("Life Support Rating: {0}".format(result))


