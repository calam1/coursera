#python3
import sys

def binary_search(a, x):
    # write your code here
    low = 0
    high = len(a) - 1
    while low <= high: 
        mid = (low + high) // 2
        mid_value = a[mid]
        if x < mid_value:
            high = mid - 1
        elif x > mid_value:
            low = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

