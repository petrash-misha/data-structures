from DoubleList import DoubleList

class Stack:
    def __init__(self):
        self.list = DoubleList()

    def push(self, data):
        self.list.add(data)

    def pop(self):
        if self.list.elementsCount() == 0:
            return None
        
        node = self.list.get(self.list.elementsCount() - 1)
        self.list.delete(self.list.elementsCount() - 1)
        
        return node
    
s = Stack()

s.push('first')
s.push('second')
s.push('third')
s.push('fouth')
s.push('fifth')
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
