import math
import random

def brute_force(X, n):
    min_d = distance(X[0], X[1])

    for i, (x, y) in enumerate(X):
         for j in range(i+1, n):
             if distance(X[i], X[j]) < min_d:
                 min_d = distance(X[i], X[j])
    return min_d



def distance(a, b):
    return math.sqrt(math.pow( (a[0]-b[0]), 2 ) + math.pow( (a[1]-b[1]),2 ) )


# this looks to be quadratic still, just another way to do a for loop, but looks nice and succint
def closest_point(points):
    distances = []

    # calculation for distance
    def distance(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2)

    for point in points:
        buffer = points[:]
        buffer.remove(point)
        #print('removed buffer {}'.format(buffer))
        distances.append(
                    distance(point, min(buffer, key=lambda x: distance(x, point)))
                )

        #print('distances {}'.format(distances))
    return min(distances)

# this was hard and I still can't get my head around it
# explanation https://www.youtube.com/watch?v=3pUOv_ocJyA&index=17&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V
# https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2
#def solution(x, y):
def solution(a):
    #a = list(zip(x, y))  # This produces list of tuples
    ax = sorted(a, key=lambda x: x[0])  # Presorting x-wise
    ay = sorted(a, key=lambda x: x[1])  # Presorting y-wise
    p1, p2, mi = closest_pair(ax, ay)  # Recursive D&C function
    return mi

def closest_pair(ax, ay):
    ln_ax = len(ax)  # It's quicker to assign variable
    if ln_ax <= 3:
        return brute(ax)  # A call to bruteforce comparison
    mid = ln_ax // 2  # Division without remainder, need int
    Qx = ax[:mid]  # Two-part split
    Rx = ax[mid:]
    # Determine midpoint on x-axis
    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()
    for x in ay:  # split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
           Qy.append(x)
        else:
           Ry.append(x)
    # Call recursively both arrays after split
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)
    # Determine smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    # Call function to account for points on the boundary
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
    # Determine smallest distance for the array
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:  # Update min_dist and points
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi

import math
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)  # store length - quicker
    mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array
    # Create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta  # assign best value to delta
    ln_y = len(s_y)  # store length of subarray for quickness
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best



############ Test Data ###############
points = [(4,4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2),
        (-2, 4)]

print('brute force closest points data from pdf     {}'.format(brute_force(points, len(points))))
print('more elegant quad perf closest data from pdf {}'.format(closest_point(points)))
print('n log n closest points data from pdf         {}'.format(solution(points)))
