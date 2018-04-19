#python3
import random

def quick_sort(myList, start, end):
    if start >= end:
        return
    k = random.randint(start, end)

    myList[k], myList[start] = myList[start], myList[k]

    less_than, greater_than = partition(myList, start, end)
    quick_sort(myList, start, less_than - 1)
    quick_sort(myList, greater_than + 1, end)

def partition(myList, start, end):
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


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist, 0, len(alist)-1)
print(alist)
