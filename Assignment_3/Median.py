def median(X, Y, length):
    i, j = length - 1, 0
    while X[i] > Y[j] and i > -1 and j < length:
        X[i], Y[j] = Y[j], X[i]
        i -= 1
        j += 1

    X.sort()
    Y.sort()

    return (X[-1] + Y[0]) >> 1
