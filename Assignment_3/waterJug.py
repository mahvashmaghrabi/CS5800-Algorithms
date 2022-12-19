import random


def swap(array, i, j):
    k = array[i]
    array[i] = array[j]
    array[j] = k


def partition(array, lo, hi, pivot):
    partition_index = lo
    j = lo
    while j < hi:
        if array[j] < pivot:
            swap(array, partition_index, j)
            partition_index = partition_index + 1
        elif array[j] == pivot:
            swap(array, j, hi)
            j = j - 1
        j = j + 1

    swap(array, partition_index, hi)
    return partition_index


def pairs(red, blue, lo, hi):

    if lo >= hi:
        return

    r = random.randint(lo, hi)
    random_jug = blue[r]
    pivot = partition(red, lo, hi, random_jug)
    partition(blue, lo, hi, random_jug)
    pairs(red, blue, lo, pivot - 1)
    pairs(red, blue, pivot + 1, hi)


if __name__ == '__main__':
    red = [10, 20, 30, 40, 80, 70, 60, 100, 90, 50]
    blue = [40, 20, 30, 10, 100, 90, 80, 60, 50, 70]

    pairs(red, blue, 0, len(blue) - 1)

    print("RED - ", red)
    print('BLUE - ', blue)



