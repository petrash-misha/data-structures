class Node:
    def __init__(self, data, prevNode, nextNode):
        self.data = data
        self.next = nextNode
        self.prev = prevNode

class DoubleList:
    def __init__(self):
        self.root = None
        self.tail = None
        self.count = 0

    def add(self, data):
        node = Node(data, None, None)
        
        if self.root == None:
            self.root = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1
            
    def get(self, n):
        return self._get(n).data

    def update(self, n, data):
        self._get(n).data = data

    def insert(self, n, data):
        if n == 0:
            node = Node(data, None, self.root)
            self.root.prev = node
            self.root = node 
            self.count += 1

        elif n == self.count:
            self.add(data)

        elif n > 0 and n < self.count:
            prev_node = self._get(n - 1)
            next_node = prev_node.next
            prev_node.next = next_node.prev = Node(data, prev_node, next_node)            
            self.count += 1
            
        else:
            raise f'N = {n} is out of range = [0, {self.count}]'

    def delete(self, n):
        if self.root == None:
            return
        elif n == 0:
            self.root = self.root.next
            if self.root != None:
                self.root.prev = None
            else:
                self.tail = None

        elif n == self.count - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        elif n > 0 and n < self.count - 1:
            prev_node = self._get(n - 1)
            next_node = prev_node.next.next
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            raise f'N = {n} is out of range = [0, {self.count}]'

        self.count -= 1

    def clean(self):
        self.__init__()
        

    def elementsCount(self):
        return self.count

    def toArray(self):
        array = []
        lastNode = self.root
        while lastNode != None:
            array.append(lastNode.data)
            lastNode = lastNode.next
                
        return array


    def _get(self, n):
        if n < 0 or n >= self.elementsCount():
            raise f'N = {n} is out of range = [0, {self.count}]'
        elif n < self.elementsCount()/2:
            lastNode = self.root
            count = 0

            while count < n:
                lastNode = lastNode.next
                count += 1
                
            return lastNode
        else:
            lastNode = self.tail
            count = self.elementsCount() - 1

            while count > n:
                lastNode = lastNode.prev
                count -= 1
                
            return lastNode


    
         



passed = 0
failed = 0

l = DoubleList()

l.add('Misha')
l.add('Mama')
l.add('Sereja')
l.add('Papa')

print('Running test: "toArray"')
if (l.toArray() == ['Misha', 'Mama', 'Sereja', 'Papa']):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')


print('Running test: "amount of elements"')
if (l.elementsCount() == 4):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')


print('Running test: "get 0"')
if (l.get(0) == 'Misha'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')


print('Running test: "get 3"')
if (l.get(3) == 'Papa'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')
    

print('Running test: "get 1"')
if (l.get(1) == 'Mama'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')


print('Running test: "get 2"')
if (l.get(2) == 'Sereja'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')






l.update(0, "Kolia")
print('Running test: "update 0"')
if (l.get(0) == 'Kolia'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')


l.update(2, "Misha")
print('Running test: "update 2"')
if (l.get(2) == 'Misha'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')


l.update(3, "Sasha")
print('Running test: "update 3"')
if (l.get(3) == 'Sasha'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')





l.insert(0, "Andrey")

print('Running test: "insert 0"')
if (l.get(0) == 'Andrey'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')

l.insert(2, "Tima")

print('Running test: "insert 2"')
if (l.get(2) == 'Tima'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')

l.insert(3, "Nikolai")

print('Running test: "insert 3"')
if (l.get(3) == 'Nikolai'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')



l.delete(0)
print('Running test: "delete 0"')
if (l.get(0) == 'Kolia'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')

l.delete(2)
print('Running test: "delete 2"')
if (l.get(2) == 'Mama'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')

print(l.get(3))
print('Running test: "delete 3"')
if (l.get(3) == 'Misha'):
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')






l.clean()
print('Running test: "clean"')
if l.elementsCount() == 0:
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')


print('Running test: "get 0"')
is_exeption_raised = False
try:
    l.get(0)
except:
    is_exeption_raised = True

if is_exeption_raised:
    passed += 1
    print('PASSED')
else:
    failed += 1
    print('FAILED')

    


print(f'Total PASSED: {passed} from 16')
print(f'Total FAILED: {failed} from 16')
l = None


