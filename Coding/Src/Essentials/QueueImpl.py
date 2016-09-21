class QueueImpl:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)

obj = QueueImpl()
obj.__init__()
obj.push(10)
obj.push(20)
obj.push(30)
print obj.peek()
print obj.size()
print obj.items
obj.pop()
print obj.items
