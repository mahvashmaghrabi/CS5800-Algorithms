def prim(Graph, r):
    prox = []
    for i in range(len(Graph)):
        prox.append((-1, float("inf")))
    visit = []
    min_spanning_tree = []
    prox[r] = (0, 0)
    visit.append(r)

    while len(visit) < len(Graph):
        minimum_vertex = None
        minimum_value = float("inf")

        for i in range(len(Graph)):
            if i not in visit and prox[i][1] < minimum_value:
                minimum_vertex = i
                minimum_value = prox[i][1]
        min_spanning_tree.append((minimum_vertex, minimum_value))
        visit.append(minimum_vertex)

        for i in range(len(Graph)):
            if i not in visit and Graph[minimum_vertex][i] < prox[i][1]:
                prox[i] = (minimum_vertex, Graph[minimum_vertex][i])
    return min_spanning_tree
