arr = [1,5,10,3,2,7,9,12,8]

def selection_sort(arr):
    n = len(arr)
    k = 0
    for i in range(n):
        #min_value = float('inf')
        min_value = arr[k]
        min_value_idx = 0
        for j in range(k,n):
            if arr[j] <= min_value:
                min_value = arr[j]
                min_value_idx = j
        k+=1
        arr[i], arr[min_value_idx] = arr[min_value_idx], arr[i]
    return arr
print(selection_sort(arr))