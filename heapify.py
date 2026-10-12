import heapq
arr=list(map(int,input("Enter element").split()))
heapq.heapify(arr)
print("Heapified array:",arr)
value=int(input("enter value to be inserted:"))
heapq.heappushpop(arr,value)
print("array after insertion:" , arr)
