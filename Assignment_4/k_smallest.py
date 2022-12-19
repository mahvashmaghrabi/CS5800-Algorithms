import heapq
from heapq import heappop


def k_smallest(arr, k):
    if not arr or len(arr) < k:
        exit()
    heapq.heapify(arr)
    while k > 1:
        heappop(arr)
        k = k - 1
    return arr[0]


print(k_smallest([2, 3, 3, 4, 1, 5, 1, 2, 4], 4))
