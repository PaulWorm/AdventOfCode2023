import sys, os
from collections import defaultdict
import numpy as np

def get_seeds(string: str):
    split1 = string.rstrip('\n').split(': ')
    return [int(x) for x in split1[1].split(' ') if x.isnumeric()]

def get_numbers(string: str):
    split1 = string.rstrip('\n').split(' ')
    return [int(x) for x in split1 if x.isnumeric()]

if __name__ == '__main__':
    input_file = 'Day5Input.txt'
    # input_file = 'Day5Input_test.txt'

    maps = defaultdict(list)

    with open(input_file, 'r') as f:
        curr_line = f.readline()
        seeds = get_seeds(curr_line)
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

    arr_maps = {}
    for i in range(len(maps)):
        arr = np.array((maps[i]))
        ind = np.argsort(arr[:,1])
        arr_maps[i] = np.array(arr[ind,:])



    def map_to_next(curr_stage,curr_val):
        idx = 0
        len_map = len(arr_maps[curr_stage])
        while idx < len_map and curr_val >= arr_maps[curr_stage][idx,1]:
            idx += 1
        if idx == 0:
            return curr_val
        else:
            idx -= 1
            if curr_val > arr_maps[curr_stage][idx,1] + arr_maps[curr_stage][idx,2]:
                return curr_val
            else:
                return curr_val - arr_maps[curr_stage][idx,1] + arr_maps[curr_stage][idx,0]

    def map_seed_to_soil(seed):
        curr_val = seed
        curr_stage = 0
        while curr_stage < len(arr_maps):
            # print(curr_val)
            curr_val = map_to_next(curr_stage, curr_val)
            curr_stage += 1
        return curr_val

    soils = []
    for seed in seeds:
        soils.append(map_seed_to_soil(seed))

    print(seeds)
    print(soils)
    print(min(soils))



