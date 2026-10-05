#Stack operations-push/peek/pop
stack=[]
n=int(input("enter no of elements : "))
for i in range(n):
    value = int(input("Enter value: "))
    stack.append(value)
print("Stack", stack)
print("Stack peek element: ",stack[-1])
print("Removed : ",stack.pop())
print("Stack",stack)
print("Stack peek element: ",stack[-1])