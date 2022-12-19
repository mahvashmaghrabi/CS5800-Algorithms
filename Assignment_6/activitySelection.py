def conflicting(activities):
    activities.sort(key=lambda x: x[1])

    minNum = 0
    i = 0
    for j in range(1, len(activities)):
        if activities[i][1] > activities[j][0]:
            minNum = minNum + 1
        else:
            i = j
    return minNum


if __name__ == '__main__':
    print(conflicting([(0, 1), (0, 1), (0, 1)]))
    print(conflicting([(0, 1), (1, 2)]))
    print(conflicting([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12),
                       (2, 14), (12, 16)]))
