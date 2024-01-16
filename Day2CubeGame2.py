import sys, os
import re
import numpy as np

cube_count = {'red':12,
              'green':13,
              'blue': 14}
colors = ['red','green','blue']

def is_possible(string):
    split1 = string.split(': ')
    split2 = split1[1].split('; ')
    max_shown = {'red':0,
              'green':0,
              'blue': 0}
    for s2 in split2:
        colors = re.findall(r"red|blue|green",s2)
        n_shown = re.findall(r"\d+",s2)
        for i,col in enumerate(colors):
            max_shown[col] = max(int(n_shown[i]),max_shown[col])
    power = 1
    for value in max_shown.values():
        power *= value
    return power


if __name__ == '__main__':
    input_file = 'Day2Input.txt'
    sum = 0
    with open(input_file,'r') as f:
        curr_line = f.readline()
        while curr_line:
            sum += is_possible(curr_line)
            curr_line = f.readline()
    print(sum)