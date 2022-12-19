def minAvgCompletion1(task):
    n = len(task)
    wait_time = [0] * n
    wait_time[0] = 0
    comp_time = 0
    for i in range(0, n):
        wait_time[i] = task[i] + wait_time[i - 1]
    for i in range(0, n):
        comp_time = comp_time + wait_time[i]
    average_compTime = comp_time / n
    return average_compTime


tasks = [3, 5]
result = minAvgCompletion1(tasks)
print(result)
