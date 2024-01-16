import sys, os
import numpy as np


def get_winning_numbers(winning_numbers, your_numbers):
    n_winning = 0
    for yn in your_numbers:
        if yn in winning_numbers and yn:
            n_winning += 1
    return n_winning

def split_numbers(string: str):
    split1 = string.rstrip('\n').split(': ')
    split2 = split1[1].split(' | ')
    winning_numbers = [int(x) for x in split2[0].split(' ') if x.isnumeric() ]
    your_numbers = [int(x) for x in split2[1].split(' ') if x.isnumeric() ]
    return set(winning_numbers), your_numbers

if __name__ == '__main__':
    input_file = 'Day4Input.txt'
    # input_file = 'Day4Input_test.txt'
    winning_numbers = []
    your_numbers = []
    total_worth = 0
    with open(input_file, 'r') as f:
        curr_line = f.readline()
        while curr_line:
            wn, yn = split_numbers(curr_line)
            winning_numbers.append(wn)
            your_numbers.append(yn)
            curr_line = f.readline()
    n_cards = np.ones(len(your_numbers))

    for i in range(len(your_numbers)):
        n_winning = get_winning_numbers(winning_numbers[i], your_numbers[i])
        n_winning = min(n_winning,len(n_cards)-i)
        n_cards[i+1:i+n_winning+1] += n_cards[i]

    print(sum(n_cards))