class node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertF(self, item):
        newnode = node(item)
        if self.head is None:
            self.head = newnode
        else:
            firstnode = self.head
            newnode.next = firstnode
            self.head = newnode

    def insertR(self, item):
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

    def nthtolastnode(self, n):
        if self.head is None:
            return "Empty List"
        else:
            marker1 = self.head
            marker2 = self.head
            for i in range(n-1):
                if marker2.next is not None:
                    marker2 = marker2.next
                else:
                    return "list has fewer than n nodes"
            print marker2.item
            while marker2.next is not None:
                marker1 = marker1.next
                marker2 = marker2.next
            return marker1.item


obj1 = LinkedList()
for i in range(10,100,10):
    obj1.insertR(i)
obj1.printList()
print  " "
print obj1.nthtolastnode(6)



