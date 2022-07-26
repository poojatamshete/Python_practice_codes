#iterative way
A = [1, 2, 3, 4, 5, 6, 7]
'''1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
start = start +1, end = end – 1'''

def ReverseArray(A):
    start = 0
    end = len(A)-1
    while start < end:
        A[start], A[end] = A[end],A[start]
        start+=1
        end-=1

    return A

print(ReverseArray(A))
#time complexity - O(n)

#recursive way
'''1) Initialize start and end indexes as start = 0, end = n-1 
2) Swap arr[start] with arr[end] 
3) Recursively call reverse for rest of the array.'''

def revAraayRecursively(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    revAraayRecursively(arr,start+1, end-1)


arr = [1, 2, 3, 4, 5, 6]
start = 0
end = len(arr)-1
revAraayRecursively(arr, start, end)
print(arr)