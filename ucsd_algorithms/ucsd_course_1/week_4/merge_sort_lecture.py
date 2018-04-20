def merge_sort(values):
    """
    values = [4, 5, 2, 1, 6, 3]
    merge_sort(values)
    """ 

    if len(values) <= 1:
        return values
    mid = len(values) // 2
    left = merge_sort(values[:mid])
    #print('left {}'.format(left))
    right = merge_sort(values[mid:])
    #print('right {}'.format(right))
    return merge(left, right)

def merge(left, right):
    """
    takes two sorted lists and retunns a single sorted list by comparing the elements one at a time
    left = [1, 5, 6]
    right = [2, 3, 4]
    merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    #print('in merge left value {}'.format(left))
    #print('in merge right value {}'.format(right))
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        print('left < right {}'.format([left[0]] + merge(left[1:], right)))
        return [left[0]] + merge(left[1:], right)

    print('right < left {}'.format([right[0]] + merge(left, right[1:])))
    return [right[0]] + merge(left, right[1:])

# values = [4, 5, 2, 1, 6, 3]
# nlogn
# print(merge_sort(values))

# more of a traditional merge_sort
def merge_sort_2(myList):
    length = len(myList)

    if length > 1:
        mid = length // 2

        left = myList[:mid]
        right = myList[mid:]

        merge_sort_2(left)
        merge_sort_2(right)

        i, j , k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
                k += 1
            else:
                myList[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


alist = [54,26,93,17,77,31,44,55,20]
merge_sort_2(alist)
print(alist)
