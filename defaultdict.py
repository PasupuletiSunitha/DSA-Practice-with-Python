#default dict
from collections import defaultdict
d=defaultdict(int)
n=int(input("Enter numbers of elements : "))
for i in range(n):
    key=input("enter key: ")
    d[key]+=1
print("Dictionary :",dict(d))    