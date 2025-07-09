import sys
T = int(sys.stdin.readline())
def bubble_by_ID(arr,marks,n):
    swap_count = 0
    new_arr = [0]*n
    for i in range(n):
        swap = False
        for j in range(1,n):
            if marks[j-1]<marks[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                marks[j-1],marks[j] = marks[j],marks[j-1]
                swap = True
            elif marks[j-1] == marks[j]:
                if arr[j-1] < arr[j]:
                    arr[j-1],arr[j] = arr[j], arr[j-1]
                    swap = True
            if swap:
                swap_count += 1            
    print(f"Minimum swap = {swap_count}")                
    for i in range(n):
        print(f"ID: {arr[i]}, mark: {marks[i]}")               

    

for i in range(T):
    n = int(sys.stdin.readline())
    arr_str = sys.stdin.readline().strip().split()
    arr_int = [int(x) for x in arr_str]
    marks = sys.stdin.readline().strip().split()
    marks = [int(x) for x in marks]
    pair = {}
    for i in range(n):
        pair[f'{arr_str[i]}'] = marks[i]
    bubble_by_ID(arr_int,marks,n)
exit(0)
