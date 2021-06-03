#This program has linked list implemented having insertion , deletion , traversal , reversal , get middle element
#Author: Shorya Updhayay
#Email: Shorya361@gmail.com
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        self.head=Node(value)

    def insert(self,value):
        head = self.head
        newNode=Node(value)
        while (head.next != None):
            head = head.next
        head.next=newNode

    def delete(self, value):
        head= self.head
        if head.value==value:
            self.head=head.next
            print('node deleted')
            return
        while(head.next!=None):
            if(head.next.value==value):
                head.next=head.next.next
                print('node deleted')
                return
            head=head.next
        print('node is not present in Linkded List')

    def reverseAlternative(self):
        head=self.head
        next=head.next
        head.next=None
        while(next.next!=None):
            second=next.next
            next.next=head
            head=next
            next=second
        second.next=head
        self.head=second

    def reverse(self):
        head=self.head
        prev=None
        while(head!=None):
            next=head.next
            head.next=prev
            prev=head
            head=next
        self.head=prev

    def reverseRecursively(self):
        prev=None
        current= self.head
        def reverse(prev,current):
            if not current.next:
                current.next=prev
                return current
            next=current.next
            current.next=prev
            prev=current
            return reverse(prev,next)
        self.head= reverse(prev,current)


    def findMiddle(self):
        first = self.head
        if ( not first.next):
            print('only one element: ',first.value)
            return
        second=first.next
        # print(first.value, second.next.value)
        while(second.next):
            first=first.next
            second=second.next
            if(second.next):
                second=second.next
            else: # if number of nodes are odd.
                print('middle element: ',first.value)
                return
        print('middle element: ', first.value) #if number of nodes are even.

    def printList(self):
        head= self.head
        while(head!=None):
            print(head.value,end=' ')
            head=head.next
            if head:
                print('->',end=" ")
        print()


a=LinkedList(2)
a.insert(5)
a.insert(6)
a.insert(12)
a.insert(99)
a.printList()
# a.delete(12)
# a.reverse()
a.reverseRecursively()
a.printList()
a.findMiddle()