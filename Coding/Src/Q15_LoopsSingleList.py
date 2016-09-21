class node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertF(self,item):
        newnode = node(item)
        if self.head is None:
            self.head = newnode
        else:
            firstnode = self.head
            newnode.next = firstnode
            self.head = newnode

    def insertR(self,item):
        newnode = node(item)
        if self.head is None:
            self.head = newnode
        elif self.head.next is None:
            onlynode = self.head
            onlynode.next = newnode
        else:
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next
            iterator.next = newnode

    def deleteF(self):
        if self.head is None:
            print "Nothing to delete"
        elif self.head.next is None:
            onlynode = self.head
            self.head = None
            return onlynode.item
        else:
            firstnode = self.head
            secondnode = firstnode.next
            self.head = secondnode
            return firstnode.item

    def deleteR(self):
        if self.head is None:
            print "Nothing to delete"
        elif self.head.next is None:
            onlynode = self.head
            self.head = None
            return onlynode.item
        else:
            iterator1 = None
            iterator2 = self.head
            while iterator2.next is not None:
                iterator1 = iterator2
                iterator2 = iterator2.next
            iterator1.next = None
            return iterator2.item

    def detectLoop(self):
        slowiterator = self.head
        fastiterator = self.head
        while fastiterator is not None:
            slowiterator = slowiterator.next
            fastiterator = fastiterator.next.next
            if slowiterator is fastiterator:
                return "True"
            elif fastiterator.next is None:
                return "False"


    def printList(self):
        if self.head is None:
            print "Empty List, nothing to print"
        else:
            iterator = self.head
            while iterator is not None:
                print iterator.item,
                iterator = iterator.next

    def reverseList(self):
        prev = None
        cur = self.head
        if self.head is None:
            print "Empty List"
        elif self.head.next is None:
            print "Only one element in the list."
        else:
            while cur is not None:
                nextnode = cur.next
                cur.next = prev
                prev = cur
                self.head = cur
                cur = nextnode




obj1 = LinkedList()
obj1.reverseList()
obj1.insertF(10)
obj1.reverseList()
obj1.insertF(20)
obj1.printList()
print " "
obj1.reverseList()
obj1.printList()
print " "
obj1.insertF(30)
obj1.insertR(40)
obj1.insertR(50)
obj1.printList()
print " "
obj1.reverseList()
obj1.printList()
print " "



# #print obj1.detectLoop()
# obj1.deleteF()
# obj1.printList()
# print " "
# obj1.deleteF()
# obj1.printList()
# print " "
# obj1.deleteF()
# obj1.printList()
# print " "
# print " "
#
# obj2 = LinkedList()
# obj2.insertF(10)
# obj2.insertF(20)
# obj2.insertF(30)
# obj2.printList()
# print " "
# #print obj1.detectLoop()
# obj2.deleteR()
# obj2.printList()
# print " "
# obj2.deleteR()
# obj2.printList()
# print " "
# obj2.deleteR()
# obj2.printList()
# print " "







