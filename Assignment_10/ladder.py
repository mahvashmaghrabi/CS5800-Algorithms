def minimumLadder(ht, x, y, m, n):
    if x > m or y > n:
        return - 1

    if ht[x][y] == ht[m][n]:
        return 0

    maximum_ht = 0

    for i in range(x, m + 1):

        for j in range(y, n + 1):

            if ht[x][y] > maximum_ht:
                maximum_ht = ht[x][y]

    return maximum_ht - ht[x][y] + 1


print(minimumLadder([[1, 2, 3],
                     [6, 5, 4],
                     [7, 8, 9]], 0, 0, 2, 2))

print(minimumLadder([[1, 2, 1],
                     [1, 2, 1],
                     [1, 1, 1]], 0, 0, 0, 2))
