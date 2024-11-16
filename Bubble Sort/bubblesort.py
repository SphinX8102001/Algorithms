arr = [1,5,10,3,2,7,5,9,12,8]

def bubbleSort(Arr):
    n = len(arr)
    for i in range(n):
        for j in range(1,n):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    print(arr)
bubbleSort(arr)