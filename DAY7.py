#linear data structures
'''1.arrays
2.create and display
3.insert
4.delete
5.append
5.remove'''
#create and print an array
'''arr=list(map(int,input("enter elements : ").split()))
print(*arr)'''

#access an element with index value

'''arr= list(map(int,input("enter elements : ").split()))
index = int(input("enter your index value:"))
print("element:",arr[index]+55)
print(*arr)'''

#create and insert an element print an array
'''arr=list(map(int,input("enter elements :").split()))
print(*arr)
index=int(input())
value=int(input())
arr.insert(index,value)
print(*arr)'''

#deleting
'''arr=list(map(int,input("enter elements :").split()))
print(*arr)
value=int(input())
arr.remove(value)
print(*arr)
index=int(input())
arr.pop(index)
print(*arr)'''

#search an element and return index value
'''arr=list(map(int,input().split()))
print(*arr)
value=int(input())
found=False
for i in range(len(arr)):
    if arr[i]==value:
        found = True
        print(value,"found at index:",i)
        break
    if found==false:
        print("element not in array.....!")'''

#found random elements
'''arr=list(map(int,input("enter elements:").split()))
arr[0]=min
for i in range(1,len(arr)):
    for j in range(i-1,len(arr)):
        if arr[j]<minimum:
            minimum=arr[j]
print(minimum)'''

#swap without built -ins
'''arr=list(map(int,input("enter elements:").split()))
print(*arr)
n=len(arr)
for i in range (n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr) '''  

'''arr=list(map(int,input("enter elements:").split()))
print(*arr)
n=len(arr)
for i in range (n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr) '''  

'''arr=list(map(int,input("enter elements:").split()))
print(*arr)
n=len(arr)
for i in range (n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr) '''  

