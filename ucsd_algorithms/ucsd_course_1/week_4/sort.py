#python3
import sys
import random

def partition3(myList, start, end):
    less_than = start # initialte less_than to be the part is less than the pivot
    i = start # scan the array left to right
    greater_than = end # the part that is greater than the pivot
    pivot = myList[start]

    while i <= greater_than:
        if myList[i] < pivot:
            myList[less_than], myList[i] = myList[i], myList[less_than]
            less_than += 1
            i += 1
        elif myList[i] > pivot:
            myList[i], myList[greater_than] = myList[greater_than], myList[i]
            greater_than -= 1
        else:
            i += 1

    return less_than, greater_than

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, n + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

