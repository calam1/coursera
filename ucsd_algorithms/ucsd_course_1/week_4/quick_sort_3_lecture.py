#python3
import random

def quick_sort(myList, start, end):
    if start >= end:
        return
    k = random.randint(start, end)

    # randomize the pivot point just in case you are sorting similar items, otherwise performance is
    # quadratic
    myList[k], myList[start] = myList[start], myList[k]

    left, right = partition(myList, start, end)
    quick_sort(myList, start, left - 1)
    quick_sort(myList, right + 1, end)

def partition(myList, start, end):
    pivot = myList[start]
    left = start # initialte less_than to be the part is less than the pivot
    right = end # the part that is greater than the pivot
    i = start # scan the array left to right

    # iterate through the whole list
    while i <= right:
        if myList[i] < pivot:
            myList[left], myList[i] = myList[i], myList[left]
            left += 1
            i += 1
        elif myList[i] > pivot:
            #myList[i], myList[right] = myList[right], myList[i]
            myList[right], myList[i] = myList[i], myList[right]
            right -= 1
        else:
            i += 1

    return left, right 


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist, 0, len(alist)-1)
print(alist)
