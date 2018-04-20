def quick_sort(myList, start, end):
    if start < end:
        # split in half or at pivot point
        # partition does all the work
        pivot = partition(myList, start, end)
        quick_sort(myList, start, pivot - 1)
        quick_sort(myList, pivot + 1, end)


def partition(myList, start, end):
    pivot = myList[start]
    # left is start
    left = start+1
    # right is end
    right = end
    done = False

    while not done:
        # if left index is less or equal than right index and myList[left] value is less than pivot
        # value (which is myList[start]) increment left index, this makes it smaller
        while left <= right and myList[left] <= pivot:
            left = left + 1
        # if right index is greater than or equal to left index and myList[right] value is greater
        # than pivot[start] value then decrement right index, this makes it smaller
        while right >= left and myList[right] >= pivot:
            right = right - 1
        # once all the iteration above is done and right is less than left, which means that we went
        # through the whole list, we shut off the while loop
        if right < left:
            done = True
        else:
            # swap if we did not make it through the list where right < left then we must swap,
            # since a value is not in order
            myList[left], myList[right] = myList[right], myList[left]

    print('start {} right {} myList {}'.format(start, right, myList))
    # swap start with myList[right] because all the values that are less than the pivot are
    # positionally after tye pivot which is myList[start] so we need to put it at the end
    myList[start], myList[right] = myList[right], myList[start]
    return right

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist, 0, len(alist)-1)
print(alist)

