#Use nonlocal diametetr for global access
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class TreeDiameter:
    def __init__(self): 
        self.root = None
        self.diameter = 0

    def findDiameter(self, root):
        def findHeight(root):
            if root is None:
                return 0

            leftHeight = findHeight(root.left)
            rightHeight = findHeight(root.right)
            currentDiameter = leftHeight + rightHeight

            self.diameter = max(currentDiameter, self.diameter)

            return max(leftHeight, rightHeight) + 1

        findHeight(root)
        return self.diameter
        
if __name__ == '__main__':
    tree = TreeDiameter()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.left.left = Node(6)
    tree.root.right.right.right = Node(7)
   
    ans = tree.findDiameter(tree.root)
    print(ans)
