#print a hallowsquare
'''n=int(input("enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print() '''

#print a square
'''n=int(input("enter n: "))
for i in range(n):
    for j in range(n):
        print("*",end= ' ')
    print() '''    

#print a hallow saquare with diagonal and anti-diagonaln=int(input("enter n: "))
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            print("*",end= ' ')
            else:
                        print(" " ,end= ' ')
    print()'''

#print an hour-glass
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or i==0 or i==n-1 or  i==j or i+j==n-1:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print()'''

#print butterfly
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j  or i+j==n-1:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print()'''

#print plus symbol
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j== n//2:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print()'''

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==n-1 or  j==0 or i==j:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print()'''
 
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==n-1 or  j==n-1 or i+j==n-1:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print()'''


'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or  j==0 or i+j==n-1:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print()'''

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or  j==4 or i+j==n-1:
            print("*",end= ' ')
        else:
            print(" " ,end= ' ')
    print()'''

#print a pyramid
'''n=int(input("enter n:"))
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    print("*"*(2*i-1))

print()
for i in range(1,n+1):
    print(' '*(n-i),end= ' ')
    if i==1:
        print("*")
    elif i==n:
        print("*"*(2*i-1))
    else:
        print("*"+' '*(2*i-3)+"*")'''

'''n=int(input(enter value:))
for i in range(n,0,-1):
    print(" " * (n-i),end=" ")
    print("*"*(2*i-1))'''

'''n=int(input("enter value:"))
for i in range(n):
    print(" " * (n-i),end=" ")
    print("*"*(2*i-1))'''

    
   





 




