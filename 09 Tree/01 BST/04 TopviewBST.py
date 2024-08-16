from collections import deque

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def topView(root):
    if not root:
        return []
    q = deque()
    d = dict()
    root.level = 0
    q.append(root)
    while q:
        node = q.popleft()
        if node.level not in d:
            d[node.level] = node.info
        if node.left:
            q.append(node.left)
            node.left.level = node.level - 1
        if node.right:
            q.append(node.right)
            node.right.level = node.level + 1
    top_view_elements = [d[i] for i in sorted(d)]
    return top_view_elements

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.left = Node(8)

    top_view = topView(tree.root)
    print("Top view of the tree:", top_view)
