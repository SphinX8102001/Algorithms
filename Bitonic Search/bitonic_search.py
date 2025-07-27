def FindPeak(arr):
    low = 0
    high = len(arr)-1
    if len(arr)==1:
        return 0     
    while low <= high:
        mid = (low + high)//2
        if mid > 0 and mid < high:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                peak = mid
                return peak
            elif arr[mid+1]>arr[mid]:
                low = mid + 1
            elif arr[mid-1] > arr[mid]:
                high = mid - 1
        elif mid == 0:
            return 0 if arr[0] > arr[1] else 1
        elif mid == high:
            return high if arr[high] > arr[high - 1] else high - 1
    
    return -1
def AscendingBinarySearch(arr,target,low,high): #choto theke boro er jonno 
    while low <=high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        elif target  < arr[mid]:
            high = mid - 1
    return -1             

def DescendingBinarySearch(arr,target,low,high): #boro theke choto er jonne binary search
    while low <=high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            high = mid - 1
        elif target  < arr[mid]:
            low = mid + 1
    return -1             

def BitonicSearch(arr,target):
    index_of_peak_element = FindPeak(arr)
    if target == arr[index_of_peak_element]:
        return index_of_peak_element
    else:
        index_of_target_element = AscendingBinarySearch(arr,target,0,index_of_peak_element)
        if index_of_target_element == -1:
            index_of_target_element = DescendingBinarySearch(arr,target,index_of_peak_element+1,len(arr)-1)
    return index_of_target_element    

arr = [1, 3, 8, 12, 9, 5, 2]
target = int(input("Target : "))
index_of_target_element = BitonicSearch(arr,target)
print(index_of_target_element)