def maxSubArray(A):
    current_sum = maximum_sum = A[0]
    for n in A[1:]:

        current_sum = max(n, current_sum+n)
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


print(maxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
