# Uses python3
import sys
from operator import itemgetter

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    pointers_start_end_list = [0] * (len(starts) + len(ends) + len(points)) # before i had empty array and used append, that was really slow, due to reallocating space on large datasets

    index = 0
    for i in range(len(starts)):
        pointers_start_end_list[index] = (starts[i], 'l')
        index += 1

    for i in range(len(ends)):
        pointers_start_end_list[index] = (ends[i], 'r')
        index += 1

    for i in range(len(points)):
        pointers_start_end_list[index] = (points[i], 'p', i) # I added index before in the for loop below I was looking up index of pointer value, that was too slow
        index += 1

    #pointers_start_end_list.sort(key=lambda x: x[0])
    p_s_e_list = sorted(pointers_start_end_list, key=itemgetter(0, 1))
    #print('list of {}'.format(pointers_start_end_list))

    l_counter = 0
    #for i in pointers_start_end_list:
    for i in p_s_e_list:
        if i[1] == 'l':
            l_counter += 1
        elif i[1] == 'p':
            cnt[i[2]] = l_counter
        elif i[1] == 'r':
            l_counter -= 1

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #print('starts {}'.format(starts))
    #print('ends {}'.format(ends))
    #print('points {}'.format(points))
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

