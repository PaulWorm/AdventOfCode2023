import sys, os
import numpy as np

if __name__ == '__main__':
    input_file = 'Day3Input.txt'
    # input_file = 'Day3Input_test.txt'
    engine_schematic = []
    with open(input_file, 'r') as f:
        curr_line = f.readline()
        while curr_line:
            es_list = [*curr_line]
            if es_list[-1] == '\n':
                es_list = es_list[:-1]
            engine_schematic.append(es_list)
            curr_line = f.readline()
    engine_schematic = np.array(engine_schematic)

    symbols = {'*'}
    m,n = engine_schematic.shape

    def get_number(k,l, seen):
        r = 0
        while l+r < n and engine_schematic[k,l+r].isnumeric():
            r += 1

        left = 0
        while l-left >= 0 and engine_schematic[k,l-left].isnumeric():
            left += 1
        if left > 0: left -= 1
        number = int(''.join(engine_schematic[k,l-left:l+r]))
        for i in range(l-left,l+r):
            seen.add((k,i))
        return number, seen

    def check_neighbours(i,j):
        neighbours = [[i+1,j],[i-1,j],[i,j+1],[i,j-1],[i-1,j-1],[i+1,j+1],[i+1,j-1],[i-1,j+1]]
        n_neighbours = 0
        numbers = []
        seen = set()
        for k,l in neighbours:
            if 0<= k < m and 0<= l < n:
                if engine_schematic[k,l].isnumeric() and (k,l) not in seen:
                    n_neighbours += 1
                    number, seen = get_number(k,l, seen)
                    numbers.append(number)
        if n_neighbours == 2:
            return numbers[0] * numbers[1]
        else:
            return 0


    sum_parts = 0
    for i in range(m):
        for j in range(n):
            if engine_schematic[i,j] in symbols:
                number = check_neighbours(i,j)
                sum_parts += number
    print(sum_parts)
