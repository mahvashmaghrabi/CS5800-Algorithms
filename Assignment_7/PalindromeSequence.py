def longestCommonSubsequence(A, B):

    x = len(A)
    y = len(B)
    L = [[0] * (x + 1)] * (y + 1)

    for i in range(y + 1):
        for j in range(y + 1):

            if i == 0 or j == 0:
                L[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    ind = L[x][y]
    char = ["\n"] * (ind + 1)
    i, j = x, y

    while i > 0 and j > 0:

        if A[i - 1] == B[j - 1]:
            char[ind - 1] = A[i - 1]
            i -= 1
            j -= 1
            ind -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result = ""

    for k in range(len(char)):
        result += char[k]

    return result


def longestPalindromeSubsequence(str):
    reverse = str[:: -1]

    return longestCommonSubsequence(str, reverse)
