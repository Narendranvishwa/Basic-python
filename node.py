class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
def display(head):
  temp=head
  while temp:
      print(temp.data,end="->")
      temp=temp.next
print("None")
print("original linked list")
display(head)

      
print("\n Insertion at the beginning")
new_node=Node(5)
new_node.next=head
head=new_node
display(head)


print("\n Insertion in the middle")
new_node=Node(25)
temp=head
while temp.data!=20:
   temp=temp.next
   new_node.next=temp.next
temp.next=new_node
display(head)


print("\n Insertion at the end")
new_node=Node(40)
temp=head
while temp.next:
    temp=temp.next
temp.next=new_node
display(head)


print("\n deletion at beginning")
head=head.next
display(head)


print("\n deletion in the middle")
temp=head
while temp.next.data!=25:
    temp=temp.next
temp.next=temp.next.next
display(head)


print("\n deletion at end")
temp=head
while temp.next.next:
    temp=temp.next
temp.next=None
display(head)
