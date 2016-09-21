# A stack can be implemented using a list.
# Inserting at end of list -> constant time because size of list can be maintained.
# Removing from end of list -> constant time because size of list can be maintained.
class StackImpl:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.size = self.size+1
        self.items.append(item) #O(1)
    def pop(self):
        return self.items.pop() #O(1)
    def peek(self):
        return self.items[len(self.items) - 1]  #
    def size(self):
        return len(self.items)

obj = StackImpl()
obj.__init__()
obj.push(10)
obj.push(20)
obj.push(30)
print obj.peek()
print obj.size()
print obj.items
obj.pop()
print obj.items
