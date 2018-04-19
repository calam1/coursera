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
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

values = [4, 5, 2, 1, 6, 3]
# nlogn
print(merge_sort(values))
