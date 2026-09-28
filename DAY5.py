
#mat approc=ach
'''n=int(input("nuber:"))
area = 3.14159 * n* n 
cir = 2*3.14159*n
print("area:",area)
print("circumference:",cir)  '''


'''import math
n=int(input("number:"))
sum = 0

for i in range(1, n + 1):
    fact = fact * i
    sum+=math.factorial(i)/(i+1)

print(sum)'''

#math approach series expression
'''n=int(input())
s=0
f=1
for i in range(1,n+1):
    f*=i
    s+=f/(i+1)
print(s)    '''

#naive approach max of list
'''arr=list(map(int,input("enter elements:").split()))
arr[0]=max
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]>maximum:
            maximum=arr[j]
print(maximum)'''

#anagram code
str1 = input("Enter first string: ").lower().replace(" ","")
str2 = input("Enter second string: ").lower().replace(" ","")
if len(str1)==len(str2):
    if sorted(str1) == sorted(str2):
    print(str1,"is anagram with",str2)
else:
    print("str1, "is not anagram with",)

