#python3

def edit_distance(s, t):
    solution = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]

    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i == 0:
                solution[i][j] = j
            elif j == 0:
                solution[i][j] = i
            elif s[i-1] == t[j-1]:
                solution[i][j] = solution[i-1][j-1]
            else:
                solution[i][j] = 1 + min(solution[i][j-1],
                                        solution[i-1][j],
                                        solution[i-1][j-1])
    #print(solution)
    return solution[len(s)][len(t)]

def edit_distance_recursion(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return edit_distance_recursion(str1, str2, m-1, n-1)
    else:
        return 1 + min(edit_distance_recursion(str1, str2, m, n - 1), edit_distance_recursion(str1, str2, m -
            1, n), edit_distance_recursion(str1, str2, m - 1, n - 1))




if __name__ == "__main__":
    a = input()
    b = input()
    print(edit_distance(a, b))
    print(edit_distance_recursion(a, b, len(a), len(b)))

