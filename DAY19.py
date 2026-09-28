#circular linked list
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("enter values: ").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head

start = int(input("enter the starting node value: "))
current=head
while current.data!=start:
    current=current.next
    if current==head:
        print("value not found")
        exit()
temp=current
print("traversal: ")
while True:
    print(temp.data, end=" ")
    temp=temp.next
    if temp==current:
        break'''



'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("enter values: ").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head

start = int(input("enter the starting node value: "))
current=head
for i in range(pos-1):
    current=current.next
print("Traversal :")
temp=current
print("traversal: ")
while True:
    print(temp.data, end=" ")
    temp=temp.next
    if temp==current:
        break'''

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("enter values: ").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head
x=int(input("enter value to be deleted: "))
current=head
previous=tail
while True:
    if current.data==x:
        if current==current.next:
            head==None
        elif current==head:
            head=head.next
            tail.next=head
        else:
            previous.next=current.next
        break
    
print("traversal: ")
if head is None:
    print("CLL Empty")
else:
    print("After deletion")
    current=head
    while True:
        print(current.data,end=" ")
        current=current.next
        if current==head:
            break


