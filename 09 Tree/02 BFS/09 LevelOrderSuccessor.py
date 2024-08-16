from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class LevelOrderTraversal:
    
    def __init__(self): 
        self.root = None

    def find_successor(self, root, target):
        if root is None:
            return None
        queue = [root]
        while len(queue) != 0:
            current = queue.pop(0)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            if current.data == target:
                break
        return queue[0].data if len(queue) != 0 else None
    
if __name__ == '__main__':
    tree = LevelOrderTraversal()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    target = 5
    successor = tree.find_successor(tree.root, target)
    print(f"The level order successor of {target} is {successor}")
