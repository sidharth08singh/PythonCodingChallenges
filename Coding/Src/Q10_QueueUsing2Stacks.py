class algorithms:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,item):
        if self.stack1 != []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(item)
            while self.stack2 != []:
                self.stack1.append(self.stack2.pop())
        else:
            self.stack1.append(item)
    def pop(self):
        return self.stack1.pop()
    def peek(self):
        return self.stack1[len(self.stack1)-1]
    def size(self):
        return len(self.stack1)
    def isEmpty(self):
        return self.stack1 == []

obj = algorithms()
print  obj.isEmpty()
print  obj.push(1)
print  obj.push(2)
print  obj.push(3)
print  obj.push(4)
print  obj.size()
print  obj.peek()
print  obj.pop()
print  obj.peek()
print  obj.pop()
print  obj.pop()
print  obj.pop()
print  obj.isEmpty()