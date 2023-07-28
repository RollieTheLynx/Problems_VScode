# -*- coding: utf-8 -*-
"""

"""

class Node:
    def __init__(self, data):
        '''
        We just create a Node class and add assign
        a value to the node.
        This becomes tree with only a root node.'''
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        '''To insert into a tree we use the same node class created above and add a insert class to it. 
        The insert class compares the value of the node to the parent node 
        and decides to add it as a left node or a right node. 
        Finally the PrintTree class is used to print the tree.'''
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, root):
        # Left -> Root -> Right
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        # Root -> Left ->Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        # Left ->Right -> Root
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
'''
  12
 6 14
3
'''

print(root.inorderTraversal(root))      
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))
