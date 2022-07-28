#using sorting algorithm
N = 5
arr = [0, 2, 1, 2, 0]
for i in range(0, N):
    for j in range(i+1, N):
        if arr[i]> arr[j]:
            arr[j], arr[i] = arr[i], arr[j]
print(arr)


#second approach
'''
1.traverse through array then count number of time 0,1,2 accurred and then store them in some variables then traverse that array insert zeros ones an 2s by adding loop on teir count 
'''
arr = [0, 2, 1, 2, 0]
zeros = 0
one = 0
two = 0
for i in arr:
    if i == 0:
        zeros+=1
    if i == 1:
        one+=1
    if i == 2:
        two+=1
i = 0

for j in range(zeros):
    arr[i] = 0
    i+=1

for j in range(one):
    arr[i] = 1
    i+=1
for j in range(two):
    arr[i] = 2
    i+=1
print(arr)


#third approach

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
low = 0
mid = 0
high = len(arr)-1

while mid<=high:
    if arr[mid]==0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low+=1
        mid+=1
    if arr[mid]==1:
        mid+=1
    if arr[mid]==2:
        arr[high], arr[mid] = arr[mid], arr[high]
        high-=1
print(arr)

#time complexity - O(n)
#space complexity - O(1)