def KthSmallest(arr):
    if len(arr)>1:
        l = 0
        h = len(arr)-1

        mid = (h+(h-l))//2
        left = arr[:mid]
        right = arr[mid:]
        KthSmallest(left)
        KthSmallest(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr

arr = [7,4,5,65,22,53,1,90,20]
n = len(arr)
ele = 3
result = KthSmallest(arr)
print(result[ele])


