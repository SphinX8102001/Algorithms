def Kadane(arr):
    current_sum = max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f'Maximum sum: {Kadane(arr)}')

