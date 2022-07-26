#simple linear search

class pair:
    def __int__(self):
        self.min = 0
        self.max = 0

def getMinMax(arr : list, n: int)->pair:
    minmax = pair()

    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]

    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]
    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    for i in range(2, n):
        if arr[i]>minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

arr = [3, 5 ,1, 6, 4, 9, 2]
n = len(arr)
result = getMinMax(arr, n)
print(result.min)
print(result.max)

#time complexity - O(n)
#space complexity - O(1)


#compair in pairs
'''If n is odd then initialize min and max as first element. 
If n is even then initialize min and max as minimum and maximum of the first two elements respectively. 
For rest of the elements, pick them in pairs and compare their 
maximum and minimum with max and min respectively. '''

def getMinMax1(arr1):
    n = len(arr1)
    if(n%2==0):
        mn = min(arr1[0], arr1[1])
        mx = max(arr1[0], arr1[1])
        i = 2
    else:
        mn = arr1[0]
        mx = arr1[1]
        i = 1

    while (i < n-1):
        if arr1[i] < arr1[i+1]:
            mn = min(mn, arr1[i])
            mx = max(mx, arr1[i+1])
        else:
            mn = min(mn, arr1[i+1])
            mx = max(mx, arr1[i])
        i+=2
    return (mn, mx)

arr1 = [3, 5 ,1, 6, 4, 9, 2]
result = getMinMax1(arr1)
print(result)
#time complexity - O(n)
#space complexity - O(1)