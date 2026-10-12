import heapq
arr=list(map(int,input("Enter element").split()))
heapq.heapify(arr)
print("Heapified array:",arr)
value=int(input("enter value to be replaced:"))
heapq.heapreplace(arr,value)
print("array after replacement:" , arr)
