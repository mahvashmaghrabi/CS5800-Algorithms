def findPeak(A):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or A[mid] > A[mid-1]) and (mid == len(A)-1 or A[mid] > A[mid + 1]):
            return mid

        elif mid > 0 and A[mid - 1] > A[mid]:
            right = mid - 1

        elif mid < len(A) - 1 and A[mid + 1] > A[mid]:
            left = mid + 1


print(findPeak([7, 2, 6, 4, 9, 8, 5, 3, 1]))
