#Creating structure of the Tree
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

#Creating the Tree Structure
class Tree:
    #Creating a Node
    def createNode(self,data):
        return Node(data)
    
    
    #Inserting a Node
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    

    #finding height of the tree
    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1


    
    #Inorder Traversal(left,root,right)
    def traverse_Inorder(self,root):
        if root is not None:
            self.traverse_Inorder(root.left)
            print(root.data,end='->')
            self.traverse_Inorder(root.right)


    #Preorder Traversal(root,left,right)
    def traverse_Preorder(self,root):
        if root is not None:
            print(root.data,end='->')
            self.traverse_Inorder(root.left)
            self.traverse_Inorder(root.right)


    #Postorder Traversal(left,right,root)
    def traverse_Postorder(self,root):
        if root is not None:
            self.traverse_Inorder(root.left)
            self.traverse_Inorder(root.right)
            print(root.data,end='->')

    #level Order traversal
    #https://www.youtube.com/watch?v=568Jr8Fs6jQ&list=PLPdtS77PaSutvrLxZJT5gmASGSed0dO_T&index=8
    def level_order_Traversal(self,root):
        q=[]
        q.append(root)
        while q:
            root= q.pop(0)
            print(root.data,end='->')
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)

'''
 # Inorder Traversal(left, root, right)
    def traverse_Inorder(self, root):
        result = []
        self._inorder_helper(root, result)
        print('->'.join(map(str, result)))

    def _inorder_helper(self, root, result):
        if root is not None:
            self._inorder_helper(root.left, result)
            result.append(root.data)
            self._inorder_helper(root.right, result)

    # Preorder Traversal(root, left, right)
    def traverse_Preorder(self, root):
        result = []
        self._preorder_helper(root, result)
        print('->'.join(map(str, result)))

    def _preorder_helper(self, root, result):
        if root is not None:
            result.append(root.data)
            self._preorder_helper(root.left, result)
            self._preorder_helper(root.right, result)

    # Postorder Traversal(left, right, root)
    def traverse_Postorder(self, root):
        result = []
        self._postorder_helper(root, result)
        print('->'.join(map(str, result)))

    def _postorder_helper(self, root, result):
        if root is not None:
            self._postorder_helper(root.left, result)
            self._postorder_helper(root.right, result)
            result.append(root.data)
'''




#Driver Code
tree = Tree()
root = tree.createNode(5)
print(root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7) 
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

tree.traverse_Inorder(root)
print(" ")
tree.traverse_Preorder(root)
print(" ")
tree.traverse_Postorder(root)
print(" ")
print("height:",tree.height(root))
print(" ")
tree.level_order_Traversal(root)