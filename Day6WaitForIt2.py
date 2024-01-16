import sys, os
import numpy as np

def parse_input(fname):
    with open(fname) as file:
        time_string = file.readline()
        curr_record_string = file.readline()
    times = time_string.split(': ')[1].replace(' ','')
    records = curr_record_string.split(': ')[1].replace(' ','')
    return int(times), int(records)

if __name__ == '__main__':
    input_file = 'Day6Input.txt'
    # input_file = 'Day6Input_test.txt'
    time, record = parse_input(input_file)
    time, record = float(time), float(record)
    hold_time = np.arange(time)
    distance = hold_time * (time-hold_time)
    is_winning = distance > record
    sol = sum(is_winning)
    print(sol)
    # sol = get_winning(time,record)
    # print(sol)

    #%%
    t_hold = +time - np.sqrt(time**2/4-record)
    t_hold2 = +time + np.sqrt(time**2/4-record)
    print(np.floor(t_hold2) - np.ceil(t_hold))
