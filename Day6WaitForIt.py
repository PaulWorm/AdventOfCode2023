import sys, os
import numpy as np

def parse_input(fname):
    with open(fname) as file:
        time_string = file.readline()
        curr_record_string = file.readline()
    times = [int(x.rstrip('\n')) for x in time_string.split(': ')[1].split(' ') if x.rstrip('\n').isnumeric()]
    records = [int(x) for x in curr_record_string.split(': ')[1].split(' ') if x.isnumeric()]
    return times, records

if __name__ == '__main__':
    input_file = 'Day6Input.txt'
    # input_file = 'Day6Input_test.txt'
    times, records = parse_input(input_file)
    print(times)
    print(records)

    def get_winning(time,record):
        hold_time = np.arange(time)
        distance = hold_time * (time-hold_time)
        return sum(distance>record)

    sol = 1
    for time, record in zip(times, records):
        sol *= get_winning(time,record)
    print(sol)