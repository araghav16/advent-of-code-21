#https://adventofcode.com/2021/day/8

import os, sys
import itertools

valid_digits = {
    '0': 'abcefg',
    '1': 'cf',
    '2': 'acdeg',
    '3': 'acdfg',
    '4': 'bcdf',
    '5': 'abdfg',
    '6': 'abdefg',
    '7': 'acf',
    '8': 'abcdefg',
    '9': 'abcdfg',
}


def getInput():
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        signal_stream = []
        for line in file_in:
            signal = (line.strip().split('|'))
            signal_stream.append(list(map(str.strip, signal)))

    return signal_stream

def getOutputValues(signal_stream):
    '''
     For each sequence
        We want to see if a permutation of "abcdefg" is valid
    '''
    digits_output = []
    for signal in signal_stream:
        #Ensure 10 input strings are alphabetically sorted
        input = sortSignalStream(signal[0])
        output = sortSignalStream(signal[1])

        potential_seq_count = 0
        key = {}
        print("Signal Stream:  {0}".format(input))
        for possible_seq in itertools.permutations("abcdefg"):
            
            for letter in "abcdefg":
                key[letter] = possible_seq["abcdefg".index(letter)]
            
            potential_seq_count+=1
            if test_candidates(key, input):
                print("Sequence #{0}: {1}".format(potential_seq_count, key))
                decoded_output = decodeOutput(key, output)
                digits_output.append(getDigits(decoded_output))
                break

    print(digits_output)
    return sum(map(int, digits_output))

def decodeOutput(key, output):
    decoded_output = []
    for string in output.split(' '):
        pattern = ''
        for char in string:
            tmp = get_keys_from_value(key,char)
            pattern += tmp[0]
        pattern = sortSignalStream(pattern)
        decoded_output.append(pattern)
    return decoded_output

def getDigits(decodeOutput):
    digit = ''
    for string in decodeOutput:
        tmp = get_keys_from_value(valid_digits,string)
        digit += tmp[0]
    return ''.join(map(str,digit))

def test_candidates(key, input):
    for string in input.split(' '):
        pattern = ''
        for char in string:
            tmp = get_keys_from_value(key,char)
            pattern += tmp[0]
        pattern = sortSignalStream(pattern)
        #Is that a valid entry in digits
        if not pattern in valid_digits.values():
            # print("{0} is not a valid digit".format(pattern))
            return None
    return True

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


def find_unq_seq(signal_stream):
    unique_sec_occurrence = 0
    for signal in signal_stream:
        sequences = signal[1].split(' ')
        # print(sequences)
    
        for seq in sequences:
            # print(seq, len(seq))
            if len(seq) in [2,3,4,7]: #Unique sec length
                unique_sec_occurrence+=1
                
    return unique_sec_occurrence
    digits = {
        '0': 'abcdef',
        '1': 'cf',
        '2': 'acdeg',
        '3': 'acdfg',
        '4': 'bcdf',
        '5': 'abdfg',
        '6': 'abdefg',
        '7': 'acf',
        '8': 'abcdefg',
        '9': 'abcdfg'
    }


def sortSignalStream(pattern):
    pattern_list = pattern.split(' ')
    
    sorted_pattern = []
    for string in pattern_list:
        tmp = sorted(string)
        sorted_pattern.append(''.join(tmp))

    return ' '.join(sorted_pattern)


if __name__ == "__main__":
    signal_stream = getInput()
    # print(signal_stream)

    # part1 = find_unq_seq(signal_stream)
    # print("Part 1: {0}".format(part1))

    part2 = getOutputValues(signal_stream)
    print("Part 2: {0}".format(part2))







