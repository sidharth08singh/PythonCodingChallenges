class node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    def insertFront(self, item):
        newnode = node(item)
        if self.head == None:
            print "Inserting first element"
            self.head = newnode
        else:
            newnode.prev = None
            newnode.next = self.head
            self.head = newnode

    def insertRear(self, item):
        newnode = node(item)
        if self.head == None:
            print "Inserting first element"
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    def deleteFront(self):
        if self.head != None:
            temp1 = self.head
            temp2 = temp1.next
            if temp2 == None:
                self.head = None
                return temp1.item
            else:
                temp2.prev = None
                temp1.next = temp1.prev = None
                self.head = temp2
            return temp1.item
        else:
            print "Error: can't delete from empty list"

    def deleteRear(self):
        if self.head != None:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            if temp.prev == None:
                self.head = None
            else:
                temp_prev = temp.prev
                temp_prev.next = None
                temp.next = temp.prev = None
            return temp.item
        else:
            print "Error: can't delete from empty list"

    def printList(self):
        cur = self.head
        while cur != None:
            print cur.item,
            cur = cur.next

    def isEmpty(self):
        return self.head == None


obj1 = DoubleLinkedList()
obj2 = DoubleLinkedList()
obj3 = DoubleLinkedList()

# print obj1.isEmpty()
# obj1.insertFront(10)
# print obj1.printList()
# obj1.insertFront(20)
# print obj1.printList()
# obj1.insertFront(30)
# print obj1.printList()
#
# print obj2.isEmpty()
# obj2.insertRear(10)
# print obj2.printList()
# obj2.insertRear(20)
# print obj2.printList()
# obj2.insertRear(30)
# print obj2.printList()

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
