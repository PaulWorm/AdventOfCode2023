import sys, os
import re
import numpy as np

cube_count = {'red':12,
              'green':13,
              'blue': 14}
colors = ['red','green','blue']

def is_possible(string):
    split1 = string.split(': ')
    id_num = int(re.findall(r"\d+",split1[0])[0])
    split2 = split1[1].split('; ')
    max_shown = {'red':0,
              'green':0,
              'blue': 0}
    for s2 in split2:
        colors = re.findall(r"red|blue|green",s2)
        n_shown = re.findall(r"\d+",s2)
        for i,col in enumerate(colors):
            max_shown[col] = max(int(n_shown[i]),max_shown[col])

    is_possible = True
    for key in max_shown.keys():
        if max_shown[key] > cube_count[key]:
            is_possible = False
    if is_possible:
        return id_num
    else:
        return 0

if __name__ == '__main__':
    input_file = 'Day2Input.txt'
    sum = 0
    with open(input_file,'r') as f:
        curr_line = f.readline()
        while curr_line:
            sum += is_possible(curr_line)
            curr_line = f.readline()
    print(sum)