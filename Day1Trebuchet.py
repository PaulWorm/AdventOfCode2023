import sys, os
import re
import numpy as np


def get_digit(string):
    digit = float(string[re.search(r"\d", string).start()]) * 10 + float(string[::-1][re.search(r"\d", string[::-1]).start()])
    return digit

if __name__ == '__main__':
    input_file = 'Day1Input.txt'
    sum = 0

    with open(input_file,'r') as f:
        curr_line = f.readline()
        while curr_line:
            sum += get_digit(curr_line)
            curr_line = f.readline()
    print(sum)

