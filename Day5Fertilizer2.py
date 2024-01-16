import sys, os
from collections import defaultdict
import numpy as np


def get_seeds(string: str):
    split1 = string.rstrip('\n').split(': ')
    seeds = [int(x) for x in split1[1].split(' ') if x.isnumeric()]
    seeds, sranges = seeds[0::2], seeds[1::2]
    new_seeds = []
    for seed, srange in zip(seeds, sranges):
        new_seeds.extend([seed + i for i in range(srange)])
    return seeds, sranges


def get_numbers(string: str):
    split1 = string.rstrip('\n').split(' ')
    return [int(x) for x in split1 if x.isnumeric()]


if __name__ == '__main__':
    # input_file = 'Day5Input.txt'
    input_file = 'Day5Input_test.txt'

    maps = defaultdict(list)

    with open(input_file, 'r') as f:
        curr_line = f.readline()
        seeds, sranges = get_seeds(curr_line)
        curr_line = f.readline()
        ind = -1
        while curr_line:
            if 'map' in curr_line:
                ind += 1
            elif curr_line.isspace():
                pass
            else:
                maps[ind].append(get_numbers(curr_line))
            curr_line = f.readline()
    seeds = np.array(seeds)
    sranges = np.array(sranges)
    inds = np.argsort(seeds)
    seeds = seeds[inds]
    sranges = sranges[inds]

    arr_maps = {}
    for i in range(len(maps)):
        arr = np.array((maps[len(maps)-1-i]))
        ind = np.argsort(arr[:, 0])
        arr = arr[ind,:]
        arr = np.array(arr)
        arr[:, [0, 1]] = arr[:, [1, 0]]
        arr_maps[i] = arr


    def map_to_next(curr_stage, curr_val):
        idx = 0
        len_map = len(arr_maps[curr_stage])
        while idx < len_map and curr_val >= arr_maps[curr_stage][idx, 1]:
            idx += 1
        if idx == 0:
            return curr_val
        else:
            idx -= 1
            if curr_val > arr_maps[curr_stage][idx, 1] + arr_maps[curr_stage][idx, 2]:
                return curr_val
            else:
                return curr_val - arr_maps[curr_stage][idx, 1] + arr_maps[curr_stage][idx, 0]


    def map_soil_to_seed(soil):
        curr_val = soil
        curr_stage = 0
        while curr_stage < len(arr_maps):
            curr_val = map_to_next(curr_stage, curr_val)
            curr_stage += 1
        return curr_val

    def check_seed_exists(seed):
        for base_seed, srange in zip(seeds, sranges):
            if seed >= base_seed and seed < base_seed + srange:
                return True
        return False

    curr_soil = 1
    curr_seed = map_soil_to_seed(46)
    print(check_seed_exists(curr_seed))
