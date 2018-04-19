#python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    #write your code here
    segments.sort(key=lambda x: getattr(x, 'end'))
    #print('end sorted segments {}'.format(segments))

    point = segments[0].end
    lst = [point]

    for i in range(1, len(segments)):
        if point < segments[i].start: # or point > segments[i].end: # check to see if not in the segment, you don't have to check for the second part, since it is sorted by end attribute
            point = segments[i].end
            lst.append(point)

    #print('lst {}'.format(lst))

    return lst


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

