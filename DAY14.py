'''n=int(input("enter a number :"))
low=0
high=n
ans=0
while low<=high:
    mid=(low+high)//2
    if mid*mid<=n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print("sqaure root",ans)  '''

#find first occurence of a number using binary
'''arr=list(map(int,input("enter numbers").split()))
target= int(input("enter number: "))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        ans=mid
        high=mid-1
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
print("first occurence: ", ans)'''

#find a last occurence by using binary serch evaluation
'''arr=list(map(int,input("enter numbers").split()))
target= int(input("enter number: "))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        ans=mid
        low=mid+1
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
print("first occurence: ", ans)'''
