#This program has Doubly-linked list implemented having insertion , deletion , traversal , reversal , get middle element , backTraversal
#Author: Shorya Updhayay
#Email: Shorya361@gmail.com

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        self.head= Node(value)

    def insert(self,value):
        head=self.head
        while(head.next):
            head=head.next
        node=Node(value)
        node.prev=head
        head.next=node

    def delete(self,value):
        head=self.head
        if head.value==value:
            self.head=head.next
            self.head.prev=None
            print('node deleted:',value)
            return
        while(head):
            if head.value== value:
                head.prev.next=head.next
                if head.next:
                    head.next.prev=head.prev
                print('node deleted:',value)
                return
            head=head.next
        print('node is not present in this Doubly Linked List')

    def traversal(self):
        head= self.head
        while(head):
            print(head.value,end=' ')
            head=head.next
            if head:
                print('-> ',end="")
        print()

    def reverse(self):
        head=self.head
        while(head.next):
            current=head.next
            head.next=head.prev
            head.prev=current
            head=current
        head.next=head.prev
        head.prev=None
        self.head=head

    def MiddleElement(self):
        first=self.head
        if not first.next:
            print('only one element')
            return
        second=first.next
        while(second.next):
            first=first.next
            second=second.next
            if second.next:
                second=second.next
            else:
                print(first.value)
                return
        print(first.value)

    def backTraversal(self):
        head=self.head
        while head.next!=None:
            head=head.next
        while (head):
            print(head.value, end=' ')
            head = head.prev
            if head:
                print('-> ', end="")
        print()

a=DoublyLinkedList(5)
# a.insert(7)
a.insert(9)
# a.insert(12)
# a.insert(14)
# a.insert(15)
a.traversal()
a.delete(12)
a.traversal()
a.backTraversal()
a.reverse()
a.traversal()
a.MiddleElement()
