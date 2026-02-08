class Tank:    
    def __init__(self, color, damage):
        self.color = color
        self.damage = damage
        self.damage_activated = 150
        self.speed = 10


    def print_all_params(self, additional_text):
        print(f"Tank color: {self.color}")
        print(f"Tank damage: {self.damage}")
        print(f"Tank active damage: {self.damage_activated}")
        print(f"Tank speed: {self.speed}")
        print(f"additional_text: {additional_text}")
        print("-------------------------------------")
    

t = Tank("red", 50)
# t.print_all_params("hello")

t2 = Tank("green", 80)
# t2.print_all_params("bye")


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

        
class List:
    def __init__(self):
        self.root = None
        self.tale = None
        self.count = 0


    def append(self, value):
        if self.root == None:
            n1 = Node(value)
            self.root = n1
            self.tale = n1
            self.count += 1
        else:
            n2 = Node(value)
            self.tale.next = n2
            self.tale = n2
            self.count += 1
            
            


    def get(self, i):
        if i >= self.count:
            return None
        
        n = self.root
        for _ in range(i):
            n = n.next
                    
        return n.value


l = List()
l.append(5)
l.append(6)
l.append(9)
l.append(4)  

n1 = Node(5)
n2 = Node(6, n1)


print(l.get(4))



