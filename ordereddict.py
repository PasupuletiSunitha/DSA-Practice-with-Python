#ordereddict
from collections import OrderedDict
d=OrderedDict()
n=int(input("Enter number of elements : "))
for i in range(n):
    key=input("Enter key :")
    value=input("enter value : ")
    d[key]=value
print("Ordered dictionary : ,d")    