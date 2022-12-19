def designate(Graph):
    if len(Graph) % 2 != 0:
        return None

    babyface = []
    heels = []

    for j in range(0, len(Graph)):

        if sum(Graph[j]) == len(Graph) / 2:
            babyface.append(j)
        else:
            heels.append(j)

        return babyface, heels
