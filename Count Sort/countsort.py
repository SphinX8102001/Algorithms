arr = [0,1,5,10,3,2,7,5,9,12,8]
def countSort(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    count_arr = [0]*(max+1)
    for i in range(len(arr)):
        val = arr[i]
        count_arr[val] += 1
    #print(count_arr)
    for i in range(1,max+1):
        count_arr[i] += count_arr[i-1]
    #print(count_arr)
    output_arr = [0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        val = arr[i]
        output_index = count_arr[val] - 1  # Convert 1-based index to 0-based
        output_arr[output_index] = val
        count_arr[val] -= 1
    return output_arr

print(countSort(arr))