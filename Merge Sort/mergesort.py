def merge(a,b):
    arr = []
    i,j = 0,0
    while len(a) > i and len(b) > j:
        if a[i] <= b[j]:
            arr.append(a[i])
            i+=1
        elif a[i] > b[j]:
            arr.append(b[j])
            j+=1
    arr.extend(a[i:])
    arr.extend(b[j:])
    return arr
def merge_sort(a):
    mid = len(a)//2
    if len(a) == 1:
        return a
    else:
        a1 = merge_sort(a[:mid])
        a2 = merge_sort(a[mid:])
        return merge(a1,a2)

nums = [3,5,3,21,10,2,1]
print(merge_sort(nums))

