
#SLL insert at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None

values=list(map(int,input("EMter values:").split()))
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode,
        tail=newnode
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print("Tail")    '''    


#insert at beggining
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None

values=list(map(int,input("Enter values:").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print("Tail")'''


#insert at beggining and delete from end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None

values=list(map(int,input("Enter values:").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print("Tail")
if head is None:
    print("SLL is empty...")
elif head.next is None:
    head=None
else:
    curreent=head
    while current.next.next is not None:
        current=current.next
    current.next=None
print("SLL After deletion")
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print("Tail")