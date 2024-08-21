#https://www.youtube.com/watch?v=AOUCC8kylCg&list=PLw41HP7SUoAVJq0JdR222HmrJZzBPd_rN&index=1
# Creating a structure for the node.
# Initializing the node's data upon calling its constructor.
class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


# Defining class for the Binary Tree
class BinaryTree:
    
    # Assigning root as null initially. So as soon as the object will be created 
    # of this BinaryTreeTraversal class, root will be set as null.
    def __init__(self): 
        self.root = None

# main method
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)