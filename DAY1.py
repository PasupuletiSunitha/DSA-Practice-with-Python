#sum of digits of a given number
'''n=int(input("enter a number : "))
sum = 0
copy = n
while n!=0:
    digit = n%10
    sum+=digit
    n//=10
print("sum of digits of ",copy, "is" , sum)'''

#reverse a number
'''n=int(input("enter a number:"))
reverse=0
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n//=10
print(reverse) '''

#Nivens number
'''n=int(input("enter a number"))
s=0
c=n
while n!=0:
    d=n%10
    s+=d
    n//=10
if c%s==0:
    print("nivens number")
else:
    print("not nivens number") '''  

     

