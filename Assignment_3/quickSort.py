import random


def threePartition(a, l, r):

    pivot = a[l]
    i = l
    lesser = l
    greater = r
    while i <= greater:
        if a[i] < pivot:
            a[i], a[lesser] = a[lesser], a[i]
            lesser += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[greater] = a[greater], a[i]
            greater -= 1
        else:
            i += 1

    return lesser, greater


def quickSort(a, l, r):
    if l >= r:
        return

    pivot_r = random.randint(l, r)
    a[l], a[pivot_r] = a[pivot_r], a[l]
    mid_1, mid_2 = threePartition(a, l, r)
    quickSort(a, l, mid_1 - 1)
    quickSort(a, mid_2 + 1, r)


if __name__ == '__main__':
    a = [1, 2, 4, 1, 2, 4, 3]
    quickSort(a, 0, len(a) - 1)
    print(a)
