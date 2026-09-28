#double linked list
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("enter no.of nodes :"))
for i in range(n):
    data=int(input("enter value"))
    newnode=node(data)
    newnode.next=head
    if head is not none:
        head.prev=newnode
    head = newnode
print("Doubly linked list : ")
temp=head
while temp is not none:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")'''

'''class node:
    def __init__(self,data):
        self.data=None
        self.prev=None
        self.next=Data
head=None
n=int(input("enter no.of nodes :"))
for i in range(n):
    data=int(input("enter value"))
    newnode=node(data)
    newnode.next=head
    if head is none:
        head = newnode
    else:
        temp=head
        while temp.next is not none:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("doubly linked list : ")  '''

#insert at end,delete at beginning
'''if head is none:
    print("dll is empty ..........")
else:
    head=head.next
    if head is not none :
        head.prev=None
print("doubly linked list : ")
temp=head
while temp is not none:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")'''

#delete at end
if head is none:
    print("dll is empty ..........")
elif head.next is none :
    head=None
else:
    temp=head
    while temp.next is not none:
        temp=temp.next
    temp.prev.next = None
print("doubly linkd list : ")
temp=head
while temp.next is not none :
    temp.prev.next = None

    



    

    













