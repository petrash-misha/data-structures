class BinaryTree:
    SCREEN_WIDTH = 160
    
    def __init__(self):
        self.root = None
        
    def add(self, value):
        if self.root == None:
            self.root = Node(value, None)
        else:
            BinaryTree._add(self.root, value)
            self.root = BinaryTree._balance(self.root)
            self.root.parentNode = None
            BinaryTree._set_level(self.root)
            
    def delete(self, value):
        delete_node = BinaryTree._find(value, self.root)
        if delete_node == self.root:
            self.root = BinaryTree._balance(_delete_root(self.root))
            self.root.parentNode = None
        else:
            BinaryTree._delete(delete_node)
    
    def _delete_root(root):
        if root.left == None and root.right == None:
            return None
        elif root.right == None:
            return root.left
        elif root.left == None:
            return root.right
        else:
            rightestNode = _find_rightest(root.left)
            if rightestNode.parentNode != root:
                rightestNode.parentNode.right = rightestNode.left
                rightestNode.left = root.left
                
            rightestNode.right = root.right
        
            return rightestNode
        
    @staticmethod
    def _delete(currentNode):
        if currentNode == None:
            return False

        parentNode = currentNode.parentNode
        if parentNode == None:
            return False

        if currentNode.left == None and currentNode.right == None:
            if parentNode.left == currentNode:
                parentNode.left = None
            else:
                parentNode.right = None
            
        elif currentNode.left != None and currentNode.right != None:
            rightestNode = _find_rightest(currentNode.left)
            if rightestNode.parentNode != currentNode:
                rightestNode.parentNode.right = rightestNode.left
                rightestNode.left = currentNode.left

            rightestNode.right = currentNode.right
            
            parent = currentNode.parentNode
            if parent.left == currentNode:
                parent.left = rightestNode
            else:
                parent.right = rightestNode
            
        elif currentNode.left != None:
            if parentNode.left == currentNode:
                parentNode.left = currentNode.left
            else:
                parentNode.right = currentNode.left

            currentNode.left.parentNode = parentNode
        else:
            if parentNode.left == currentNode:
                parentNode.left = currentNode.right
            else:
                parentNode.right = currentNode.right

            currentNode.right.parentNode = parentNode

        grandParent = parentNode.parentNode
        if parentNode == grandParent.right:
            grandParent.right = _balance(parentNode)
            grandParent.right.parentNode = grandParent 
        else:
            topNodeOfBalancedSubtree = _balance(parentNode)
            grandParent.left = topNodeOfBalancedSubtree
            topNodeOfBalancedSubtree.parentNode = grandParent
            # it is important to call this func after we set correct parent for
            # topNodeOfBalancedSubtree as it's parent used to calculate correct level
            set_level(topNodeOfBalancedSubtree)
        return True

    @staticmethod 
    def _set_node_level(node):
        if node.parentNode == None:
            node.level = 0
        else:
            node.level = node.parentNode.level + 1

    @staticmethod        
    def _set_level(node):
        BinaryTree.bfs(node, BinaryTree._set_node_level)
        

    def dfs(currentNode, action):
        if currentNode == None:
            return
        else:
            dfs(currentNode.left)
            action(currentNode)
            dfs(currentNode.right)

    @staticmethod 
    def bfs(node, action):
        qeue = [node]
        while len(qeue) != 0:
            node = qeue.pop(0)
            if node.left != None:
                qeue.append(node.left)
            if node.right != None:
                qeue.append(node.right)
            action(node)       

    @staticmethod
    def _ll_rotation(node):
        l_node = node.left
        l_node.right = node
        node.left = None
        node.parentNode = l_node
        
        return l_node

    @staticmethod
    def _rr_rotation(node):
        r_node = node.right
        r_node.left = node
        node.right = None
        node.parentNode = r_node
        
        return r_node

    @staticmethod
    def _lr_rotation(node):
        l_node = node.left
        node.left = l_node.right
        l_node.right = None
        node.left.left = l_node
        node.left.parentNode = node
        l_node.parentNode = node.left
        return BinaryTree._ll_rotation(node)
    
    @staticmethod
    def _rl_rotation(node):
        r_node = node.right
        node.right = r_node.left
        r_node.left = None
        node.right.right = r_node
        node.right.parentNode = node
        r_node.parentNode = node.right
        return BinaryTree._rr_rotation(node)

    def find(self, value):
        return BinaryTree._find(value, self.root)

    @staticmethod    
    def _find(value, currentNode):
        if currentNode == None:
            return None
        elif currentNode.value == value:
            return currentNode
        elif currentNode.value < value:
            return BinaryTree._find(value, currentNode.left, currentNode)
        else:
            return BinaryTree._find(value, currentNode.right)

    @staticmethod
    def _add(currentNode, value):
        if value <= currentNode.value:
            if currentNode.left == None:
                currentNode.left = Node(value, currentNode)
            else:
                BinaryTree._add(currentNode.left, value)
                currentNode.left = BinaryTree._balance(currentNode.left)
                currentNode.left.parentNode = currentNode
                BinaryTree._set_level(currentNode.left)
        else:
            if currentNode.right == None:
                currentNode.right = Node(value, currentNode)
            else:
                BinaryTree._add(currentNode.right, value)
                currentNode.right = BinaryTree._balance(currentNode.right)
                currentNode.right.parentNode = currentNode
                BinaryTree._set_level(currentNode.right)
                

    @staticmethod
    def _tree_height(node):
        if node == None:
            return 0
        
        left_height = BinaryTree._tree_height(node.left)
        right_height = BinaryTree._tree_height(node.right)
        return max(left_height, right_height) + 1

    @staticmethod
    def _is_leaf(node):
        if node == None:
            return False
        if node.left == None and node.right == None:
            return True
        return False
    
    @staticmethod
    def _balance(node):        
        left_depth = BinaryTree._tree_height(node.left)
        right_depth = BinaryTree._tree_height(node.right)
        difference = abs(left_depth - right_depth)
        if difference < 2:
            return node

        initial_level = node.level
        result = None

        if left_depth > right_depth:
            if node.left.right == None:
                result = BinaryTree._ll_rotation(node)
            else:
                result = BinaryTree._lr_rotation(node)
                
        else:
            if node.right.left == None:
                result = BinaryTree._rr_rotation(node)
            else:
                result = BinaryTree._rl_rotation(node)

        return result
        

    def _find_rightest(node):
        if node.right == None:
            return node
        else:
            return _find_rightest(node.right)
                
    def update(self, old, new):
        if self.delete(old):
            self.add(new)
            return True
        return False

    def print(self):
        BinaryTree._print_bfs(self.root)
        
    @staticmethod
    def _print_bfs(node):
        array = []
        node_level = 0
        qeue = [node]
        i = 0
        while len(qeue) != 0:
            i += 1
            node = qeue.pop(0)
            if node_level == node.level:
                array.append(node)
            else:
                BinaryTree._print_line(array)
                node_level += 1
                array = [node]
            if node.value != None:
                if node.left == None:
                    qeue.append(Node(None, None, node.level + 1))
                else:
                    qeue.append(node.left)
                if node.right == None:
                    qeue.append(Node(None, None, node.level + 1))
                else:
                    qeue.append(node.right)

        BinaryTree._print_line(array)
            
                
    @staticmethod
    def _print_line(array):
        node_level = 0
        for node in array:
            if node != None:
                node_level = node.level
                break
        p = int(BinaryTree.SCREEN_WIDTH // (2 ** node_level))
        o = int(p // 2)
        line = o * ' '  
        for node in array:
            if node.value != None:
                line += str(node.value)
            else:
                line += '@'
            line += p * ' '
        
        print(line)
        print()
        
            
                
            
            

 #   def exist(self, value):
  #  def max(self):
   # def min(self):
    #def sum(self):
    #def average(self):
    #def count(self):

            
    
    
tree = BinaryTree()
tree.add(100)
tree.print()
print(100, '-'*190)
tree.add(125)
tree.print()
print(125, '-'*190)
tree.add(10)
tree.print()
print(10, '-'*190)
tree.add(175)
tree.print()
print(175, '-'*190)
tree.add(40)
tree.print()
print(40, '-'*190)
tree.add(260)
tree.print()
print(260, '-'*190)
tree.add(190)
tree.print()
print(190, '-'*190)
tree.add(15)
tree.print()
print(15, '-'*190)
tree.add(45)
tree.print()
print(45, '-'*190)
tree.add(75)
tree.print()
print(75, '-'*190)
tree.add(5)
tree.print()
print(5, '-'*190)
tree.add(8)
tree.print()
print(8, '-'*190)

tree.print()
print('-'*190)
 

#
#
#tree.add(140)
#tree.add(170)
#tree.add(180)
#tree.add(5)
#tree.add(95)
#tree.add(145)
#tree.add(190)
#print('BFS')
#print('----------------------')
#print('Finish')
#delete_node = tree.find(2)
#print(delete_node)
#tree.delete(2)
#print('-'*20)
#tree.update(14, 44)

