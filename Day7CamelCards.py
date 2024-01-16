import sys, os
from collections import Counter
import numpy as np

def get_rank(hand):
    s_hand = Counter(hand)
    if len(s_hand) == 1:
        return 6
    elif len(s_hand) == 2:
        if s_hand.most_common(1)[0][1] == 4:
            return 5
        else:
            return 4
    elif len(s_hand) == 3:
        if s_hand.most_common(1)[0][1] == 3:
            return 3
        else:
            return 2
    elif len(s_hand) == 4:
        return 1
    else:
        return 0

custom_sorting_order = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
custom_order = {c:len(custom_sorting_order)-i for i,c in enumerate(custom_sorting_order)}

def customSorted(l):
  return sorted(l, key=lambda c:custom_order.get(c, len(custom_order)))


if __name__ == '__main__':
    input_file = 'Day7Input.txt'
    # input_file = 'Day7Input_test.txt'
    hands = []
    bids = []
    with open(input_file) as file:
        curr_line = file.readline()
        while curr_line:
            hand, bid = curr_line.rstrip('\n').split(' ')
            hands.append(hand)
            bids.append(bid)
            curr_line = file.readline()
    hands = np.array(hands)
    bids = np.array(bids)

    ranks = np.array([get_rank(hand) for hand in hands])
    sort_with_rank = np.argsort(ranks)
    ranks = ranks[sort_with_rank]
    hands = hands[sort_with_rank]
    bids = bids[sort_with_rank]
    n_ranks = 7

    mat = np.zeros((len(hands),7))
    mat[:,0] = bids[:].astype(str)
    mat[:,-1] = ranks[:].astype(str)
    for i in range(len(hands)):
        mat[i,1:-1] = [custom_order[h] for h in hands[i]][::-1]

    ind = np.lexsort(mat.T)
    mat = mat[ind,:]

    sol = mat[:,0] * np.arange(1,len(hands)+1)
    print(sum(sol))


