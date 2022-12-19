def minAvgCompletion2(tasks):
    n = len(tasks)
    processing_time = []
    completion_time = []

    for j in range(n):
        processing_time.append(tasks[j][0])

    compTasks = 0
    minimum = 999
    short_pt = 0
    time = 0
    check = False

    while compTasks != n:
        for j in range(n):
            if (tasks[j][1] <= time) and (processing_time[j] < minimum) and (processing_time[j] > 0):
                minimum = processing_time[j]
                short_pt = j
                check = True

        if not check:
            time = time + 1
            continue

        processing_time[short_pt] = processing_time[short_pt] - 1
        minimum = processing_time[short_pt]
        if minimum == 0:
            minimum = 999

        if processing_time[short_pt] == 0:
            compTasks = compTasks + 1
            check = False
            y = time + 1
            temp = [short_pt, y]
            completion_time.append(temp)
        time = time + 1
    average_compTime = 0
    for j in range(n):
        average_compTime = average_compTime + completion_time[j][1]

    average_compTime = average_compTime / n
    return average_compTime


print(minAvgCompletion2([[3, 5], [5, 2]]))
print(minAvgCompletion2([[3, 5], [5, 4]]))
