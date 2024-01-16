import sys, os
import re
import numpy as np

def get_digit(string):
    set = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    regex_match = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    re_matches = re.findall(regex_match, string)
    re1, re2 = re_matches[0],re_matches[-1]
    print(string, '||',re_matches)
    # print(re1,re2)

    if re1 in set:
        d1 = set[re1]
    else:
        d1 = int(re1)

    if re2 in set:
        d2 = set[re2]
    else:
        d2 = int(re2)


    digit = d1 * 10 + d2
    print(re1, re2, digit)
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