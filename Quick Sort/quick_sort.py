def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= j and arr[i]<pivot:
            i+=1
        while i <= j and arr[j]>pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]
    arr[low],arr[j] = arr[j], arr[low]
    return j #j hocche pivot in correction postion
def quick_sort(arr,low,high):
    if low < high:
        pivot_index = partition(arr,low,high)
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)


arr = input("Enter an unsorted arr: ").split()
arr = [int(x) for x in arr]
quick_sort(arr,0,len(arr)-1)
print("Sorted Array: ",arr)        