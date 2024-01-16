import sys, os
import numpy as np


def get_winning_numbers(string: str):
    split1 = string.rstrip('\n').split(': ')
    split2 = split1[1].split(' | ')
    winning_numbers = split2[0].split(' ')
    your_numbers = split2[1].split(' ')
    winning_numbers = set(winning_numbers)
    worth = 0
    for yn in your_numbers:
        if yn in winning_numbers and yn.isnumeric():
            if worth == 0:
                worth = 1
            else:
                worth *= 2
    return worth

if __name__ == '__main__':
    input_file = 'Day4Input.txt'
    # input_file = 'Day4Input_test.txt'
    engine_schematic = []
    total_worth = 0
    with open(input_file, 'r') as f:
        curr_line = f.readline()
        while curr_line:
            total_worth += get_winning_numbers(curr_line)
            curr_line = f.readline()

    print(total_worth)