class node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def insertFront(self, item):
        newnode = node(item)
        # If list is empty
        if self.head is None:
            print "Inserting first element"
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
        # If list has one element
        elif self.head.next is self.head and self.head.prev is self.head:
            print "Inserting second element"
            onlynode = self.head
            newnode.next = onlynode
            newnode.prev = onlynode
            onlynode.next = newnode
            onlynode.prev = newnode
            self.head = newnode
        # If list has more than one element
        else:
            firstnode = self.head
            lastnode = firstnode.prev
            newnode.next = firstnode
            newnode.prev = lastnode
            firstnode.prev = newnode
            lastnode.next = newnode
            self.head = newnode

    def insertRear(self, item):
        newnode = node(item)
        # If list is empty
        if self.head is None:
            print "Inserting first element"
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
        # If list has one element
        elif self.head.next is self.head and self.head.prev is self.head:
            print "Inserting second element"
            onlynode = self.head
            newnode.next = onlynode
            newnode.prev = onlynode
            onlynode.next = newnode
            onlynode.prev = newnode
        # If list has more than one element
        else:
            firstnode = self.head
            lastnode = firstnode.prev
            newnode.prev = lastnode
            newnode.next = firstnode
            lastnode.next = newnode
            firstnode.prev = newnode

    def deleteFront(self):
        if self.head is None:
            print "Error: list is empty. nothing to delete"
        elif self.head.next is self.head and self.head.prev is self.head:
            onlynode = self.head
            self.head = None
            return onlynode.item
        else:
            firstnode = self.head
            secondnode = firstnode.next
            lastnode = firstnode.prev
            secondnode.prev = lastnode
            lastnode.next = secondnode
            self.head = secondnode
            return firstnode.item

    def deleteRear(self):
        if self.head is None:
            print "Error: list is empty, nothing to delete"
        elif self.head.next is self.head and self.head.prev is self.head:
            onlynode = self.head
            self.head = None
            return onlynode.item
        else:
            firstnode = self.head
            lastnode = firstnode.prev
            secondlastnode = lastnode.prev
            secondlastnode.next = firstnode
            firstnode.prev = secondlastnode
            return lastnode.item

    def isEmpty(self):
        return self.head is None

    def printList(self):
        # If list is empty
        if self.head is None:
            return "Empty List: nothing to print"
        # If list has only one element
        elif self.head.next is self.head and self.head.prev is self.head:
            print self.head.item,
        # If list has more than one element
        else:
            iterator = self.head
            lastnode = self.head.prev
            while iterator is not lastnode:
                print iterator.item,
                iterator = iterator.next
            print iterator.item,

obj1 = CircularLinkedList()
obj2 = CircularLinkedList()
obj3 = CircularLinkedList()

# print obj1.isEmpty()
# print obj1.printList()
# obj1.insertFront(10)
# print obj1.printList()
# obj1.insertFront(20)
# print obj1.printList()
# obj1.insertFront(30)
# print obj1.printList()


# print obj2.isEmpty()
# obj2.insertRear(10)
# print obj2.printList()
# obj2.insertRear(20)
# print obj2.printList()
# obj2.insertRear(30)
# print obj2.printList()
#
obj3.insertFront(10)
obj3.insertRear(20)
obj3.insertFront(5)
print obj3.printList()
obj3.deleteFront()
print obj3.printList()
obj3.deleteRear()
print obj3.printList()
obj3.deleteFront()
print obj3.printList()
obj3.insertRear(10)
print obj3.printList()
obj3.deleteRear()
print obj3.printList()
obj3.deleteRear()
obj3.deleteFront()
print obj3.printList()

