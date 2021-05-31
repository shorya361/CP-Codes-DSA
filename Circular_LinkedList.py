#This program has Circular-linked list implemented having insertion , deletion , traversal , reversal , get middle element
#Author: Shorya Updhayay
#Email: Shorya361@gmail.com

class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class CircularLinkedList:
    def __init__(self,value):
        self.head=Node(value)
        self.head.next= self.head
    def insert(self,value):
        head=self.head
        while(head.next!=self.head):
            head=head.next
        head.next=Node(value)
        head.next.next=self.head

    def traversal(self):
        head=self.head
        print(head.value,end="")
        head=head.next
        if head != self.head :
            print(' -> ',end="")
        while(head!=self.head):
            print(head.value,end="")
            head=head.next
            if(head!= self.head):
                print(' -> ',end="")
        print()

    def delete(self, instance):
        head=self.head
        if head.next==head:
            print('only one element')
            return
        if head.value==instance: # deletion of first node
            head=head.next
            while head.next != self.head:
                head=head.next
            head.next=head.next.next
            self.head=head.next
            print('node deleted: ',instance)
            return
        else:
            next=head.next
            while next!=self.head:
                if next.value==instance:
                    head.next=next.next
                    print('node deleted:', instance)
                    return
                head=next
                next=next.next
            print('element is not present')

    def reversal(self):
        head=self.head
        if head.next !=self.head:
            current=head.next
        else:
            return
        while current.next!= self.head:
            next=current.next
            current.next=head
            head=current
            current=next
        current.next.next=current
        current.next=head
        self.head=current

    def MiddleElement(self):
        first=self.head
        if not first.next:
            print('only one element')
            return
        second=first.next
        while(second.next != self.head):
            first=first.next
            second=second.next
            if second.next!= self.head:
                second=second.next
            else:
                print(first.value)
                return
        print(first.value)

a=CircularLinkedList(5)
# a.insert(6)
# a.insert(12)
a.insert(7)
# a.insert(9)
a.insert(14)
a.insert(15)
# a.traversal()
# a.delete(14)
# a.traversal()
# a.MiddleElement()
# a.reversal()
a.traversal()
a.reversal()
a.traversal()