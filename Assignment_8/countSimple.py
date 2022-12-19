def countSimplePath(Graph, a, b):

    if a == b:
        return 1
    else:
        value = 0

        for i in range(len(Graph)):
            if Graph[a][i] == 1:
                value += countSimplePath(Graph, i, b)
        return value
