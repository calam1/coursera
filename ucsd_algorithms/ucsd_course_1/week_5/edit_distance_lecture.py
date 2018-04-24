import math

# Insertions corresponds to the case when we selected the symbol from the second string and deletions that correspond to the case when we selected the symbol from the first string. 


def recursive_edit_dist(str1, str2, m, n):
    # if first  str is empty only option is to insert all chars of second str
    if m == 0:
        return n
    # if second str is empty only option is to remove all chars of first str
    if n == 0:
        return m

    # if last char of 2 str are same move on
    if str1[m - 1] == str2[n - 1]:
        return recursive_edit_dist(str1, str2, m - 1, n - 1)

    # if last chars are not same, conside all 3 operations on last char of
    # first str, take min of the three
    return 1 + min(recursive_edit_dist(str1, str2, m, n - 1), # insert
                   recursive_edit_dist(str1, str2, m - 1, n), # remove
                   recursive_edit_dist(str1, str2, m - 1, n - 1), # replace
            )

str1 = 'sunday' # answer should be 3
str2 = 'saturday'
#str1 = 'editing'
#str2 = 'distance'

print('recursion {}'.format(recursive_edit_dist(str1, str2, len(str1), len(str2))))


def edit_dist_dp(str1, str2, m, n):
    solution = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # if first string is empty only option is insert all chars of second str
            if i == 0:
                solution[i][j] = j
            # if second string is empty only option is to remove all chars of second str
            elif j == 0:
                solution[i][j] = i
            # if last chars are equal, go on
            elif str1[i - 1] == str2[j - 1]:
                solution[i][j] = solution[i - 1][j - 1]
            else:
                solution[i][j] = 1 + min(solution[i][j - 1], # insert
                                         solution[i - 1][j], # remove
                                         solution[i - 1][j - 1] # replace
                        )

    print(solution)
    return solution[m][n]

#str1 = 'sunday' # answer should be 3
#str2 = 'saturday'
##str1 = 'editing'
#str2 = 'distance'
print('dynamic programming {}'.format(edit_dist_dp(str1, str2, len(str1), len(str2))))
