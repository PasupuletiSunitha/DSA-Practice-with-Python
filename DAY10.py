# binary search
'''n = int(input("Enter the number fo elements: "))
arr = []
print("Elements in sorted order: ")
for i in range(n):
    arr.append(int(input()))
target = int(input("Enter the element to search: "))
left = 0
right = n-1
found = -1
while left <= right:
    mid = (left+right)//2
    if arr[mid] == target:
        found = mid
        break
    elif arr[mid]<target:
        left = mid+1
    else:
        right = mid - 1
if found != -1:
    print("Value found at index", found)
else:
    print("Value not found")'''


# binary search
n = int(input("Enter the number fo elements: "))
arr = []
print("Elements in sorted order: ")
for i in range(n):
    arr.append(input())
target = input("Enter the element to search: ")
left = 0
right = n-1
found = -1
while left <= right:
    mid = (left+right)//2
    if arr[mid] == target:
        found = mid
        break
    elif arr[mid]<target:
        left = mid+1
    else:
        right = mid - 1
if found != -1:
    print("Value found at index", found)
else:
    print("Value not found")