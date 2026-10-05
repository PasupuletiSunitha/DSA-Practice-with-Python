#Stack operations - overflow condition
stack=[]
size=int(input("Enter the size of the stack: "))
n=int(input("Enter number of elements : "))
for i in range(n):
    value=int(input("Enter value: "))
    if(len(stack)<size):
        stack.append(value)
        print("Pushed:",value)
    else:
        print("stack overflow......")
print("Stack",stack)            
