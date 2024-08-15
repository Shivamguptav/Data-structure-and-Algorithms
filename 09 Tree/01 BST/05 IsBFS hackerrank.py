def checkBST(root):
    def in_order(root,value):
        if root is None:
            return 
        in_order(root.left,value)
        value.append(root.data)
        in_order(root.right,value)
        
        
    value=[]
    in_order(root,value)
    for i in range(len(value)-1):
        if value[i]>=value[i+1]:
            return False
    return True


#Second Method--------------------------------------->

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    # create helper function
    def check(root,min_value,max_value):
        #base case
        if not root:
            return True
        #general case
        if root.data<min_value or root.data>max_value:
            return False
        return check(root.left,min_value,root.data-1) and check(root.right,root.data+1,max_value)
    return check(root,0,10000)