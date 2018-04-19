def quick_sort(myList, start, end):
    if start < end:
        pivot = partition(myList, start, end)
        quick_sort(myList, start, pivot - 1)
        quick_sort(myList, pivot + 1, end)


def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False

    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while right >= left and myList[right] >= pivot:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap
            myList[left], myList[right] = myList[right], myList[left]

    # swap start with myList[right]
    myList[start], myList[right] = myList[right], myList[start]
    return right

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist, 0, len(alist)-1)
print(alist)

