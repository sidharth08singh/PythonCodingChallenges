class node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class linkedlist(object):
    def __init__(self):
        self.head = None

    def insertFront(self,item):
        newnode = node(item)
        if self.head == None:
            print "Inserting First Element"
            self.head = newnode
            return
        newnode.next = self.head
        self.head = newnode

    def insertRear(self,item):
        newnode = node(item)
        if self.head == None:
            print "Inserting First Element"
            self.head = newnode
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newnode

    def deleteFront(self):
        if self.head != None:
            temp = self.head
            self.head = temp.next
            return temp.item
        else:
            print "Error: can't delete from empty list"

    def deleteRear(self):
        if self.head != None:
            cur = self.head
            prev = None
            while cur.next != None:
                prev = cur
                cur = cur.next
            if prev == None:
                self.head = cur.next
            else:
                prev.next = None
            return cur.item
        else:
            print "Error: can't delete from empty list"

    def printList(self):
        cur = self.head
        while cur != None:
            print cur.item,
            cur = cur.next

    def isEmpty(self):
        return self.head == None


    def

obj1 = linkedlist()
obj2 = linkedlist()
obj3 = linkedlist()

print obj1.isEmpty()
obj1.insertFront(10)
print obj1.printList()
obj1.insertFront(20)
print obj1.printList()
obj1.insertFront(30)
print obj1.printList()

print obj2.isEmpty()
obj2.insertRear(10)
print obj2.printList()
obj2.insertRear(20)
print obj2.printList()
obj2.insertRear(30)
print obj2.printList()

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







