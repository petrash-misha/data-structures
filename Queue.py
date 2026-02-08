from DoubleList import DoubleList

class Queue:
    def __init__(self):
        self.list = DoubleList()

    def push(self, data):
        self.list.add(data)

    def pop(self):
        node = self.list.get(0)
        self.list.delete(0)
        return node
    
q = Queue()

q.push('first')
q.push('second')
q.push('third')
print(q.pop())
print(q.pop())
print(q.pop())
