# python3
import sys
import itertools


# http://thisthread.blogspot.com/2018/02/partitioning-souvenirs.html
def solution(values):
    total = sum(values)
    if len(values) < 3 or total % 3:  # 1
        return False
    third = total // 3
    solution = [[0] * (len(values) + 1) for _ in range(third + 1)]  # 2

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):  # 3
            ii = i - values[j - 1]  # 4
            if values[j - 1] == i or (ii > 0 and solution[ii][j - 1]):  # 5
                solution[i][j] = 1 if solution[i][j - 1] == 0 else 2
            else:
                solution[i][j] = solution[i][j - 1]  # 6

    return True if solution[-1][-1] == 2 else False


def partition2(values):
    total = sum(values)  # add it up
    if total % 2:
        return False

    half = total // 2
    solution = [[False for _ in range(len(values) + 1)] for _ in range(half + 1)]

    for i in range(1, half + 1):
        for j in range(1, len(values) + 1):
            if values[j - 1] == i or solution[i][
                j - 1]:  # if current value is equal to row number or if the value to the left of the current [i][j] is True
                solution[i][j] = True
            else:  # get the the tentative row index in ii. If the relative cell on the left adjacent column is available and it is set to True, the current cell is set to True too.
                ii = i - values[j - 1]
                if ii > 0 and solution[ii][j - 1]:
                    solution[i][j] = True

    # print(solution)
    # return solution[-1][-1]

    return solution[half][len(values)]


def is_subset_sum(arr, n, sum):
    if sum == 0: return True
    if n == 0 and sum != 0: return False

    # if last element is greater than sum, then ignore it
    if arr[n - 1] > sum:
        return is_subset_sum(arr, n - 1, sum)
    else:  # check if sum can be obtained by including or excluding the last element
        return is_subset_sum(arr, n - 1, sum) or is_subset_sum(arr, n - 1, sum - arr[n - 1])


# this is way easier to comprehed than the partition2 function
def find_partition2(arr, n):
    sums = sum(arr)

    if sums % 2 != 0:
        return False

    return is_subset_sum(arr, n, sums // 2)


def find_partition2_dp(arr):
    sums = sum(arr)
    if sums % 2:
        return False
    half = sums // 2

    solution = [[False for _ in range(len(arr) + 1)] for _ in range(half + 1)]

    for i in range(half + 1):
        for j in range(len(arr) + 1):
            # i == 0 or j == 0 are the base cases for the recursive solution
            if i == 0:
                solution[i][j] = True
            elif j == 0: # if there are no values it has to be false
                solution[i][j] = False
            else:
                if arr[j - 1] > i:
                    solution[i][j] = solution[i][j - 1]
                else:
                    solution[i][j] = solution[i][j - 1] or solution[i - arr[j - 1]][j - 1]


    return solution[half][len(arr)]


# values = [1, 5, 11, 5]
# print('partition2 should be true {}'.format(partition2(values)))
# print('find_partition2 recursive should be true {}'.format(find_partition2(values, len(values))))
# print('find_partition2 dp should be true {}'.format(find_partition2_dp(values)))
# print('------------------')
# values2 = [1, 3, 11, 5]
# print('partition2 should be false {}'.format(partition2(values2)))
# print('find_partition2 recursive should be false {}'.format(find_partition2(values2, len(values2))))
# print('find_partition2 dp should be false {}'.format(find_partition2_dp(values2, )))


#def partition3(A):
#    for c in itertools.product(range(3), repeat=len(A)):
#        sums = [None] * 3
#        for i in range(3):
#            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
#
#        if sums[0] == sums[1] and sums[1] == sums[2]:
#            return 1
#
#    return 0

# http://thisthread.blogspot.com/2018/02/partitioning-souvenirs.html
def partition3(values):
    total = sum(values)
    if len(values) < 3 or total % 3:
        return 0
    third = total // 3
    table = [[0] * (len(values) + 1) for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):
            ii = i - values[j - 1]
            if values[j - 1] == i or (ii > 0 and table[ii][j - 1]):
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]

    #return True if table[-1][-1] == 2 else False
    return 1 if table[-1][-1] == 2 else 0

if __name__ == '__main__':
   input = sys.stdin.read()
   n, *A = list(map(int, input.split()))
   print(partition3(A))
