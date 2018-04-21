#python3

import sys

def merge_sort(mylist):
    length = len(mylist)
    if length == 1:
        return mylist, 0
    else:
        mid = length // 2
        left = mylist[:mid]
        right = mylist[mid:]

        left, ai = merge_sort(left)
        right, bi = merge_sort(right)
        c = []

        i, j  = 0, 0
        inversions = 0 + ai + bi

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                c.append(left[i])
                i += 1
            else:
                c.append(right[j])
                j += 1
                inversions += (len(left)-i) # length - i , any items after i are an inversion

        while i < len(left):
            c.append(left[i])
            i += 1

        while j < len(right):
            c.append(right[j])
            j += 1

        return c, inversions

#alist = [54,26,93,17,77,31,44,55,20]
#alist = [2, 3, 9, 2, 9]
#print(merge_sort(alist))
#print(alist)


def get_number_of_inversions(a):
    c, number_of_inversions = merge_sort(a)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a))

