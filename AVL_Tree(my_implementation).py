class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1

def insert(root, value):
    if root==None:
        return Node(value)
    if value >root.value:
        root.right= insert(root.right,value)
    else:
        root.left=insert(root.left,value)
    root.height = max(findHeight(root.left),findHeight(root.right)) +1  
    balance= CheckBalance(root) # left.height - right.height
    if balance <-1 and value<root.right.value: # R-L
        root.right=rightRotation(root.right)
        return leftRotation(root)   
    if balance <-1 and value > root.right.value:# R-R
        return leftRotation(root)
    if balance >1 and value < root.left.value:# L-L
        return rightRotation(root)
    if balance> 1 and value > root.left.value:# L-R
        root.left= leftRotation(root.left)
        return rightRotation(root)
    return root

def leftRotation(root):
    x=root
    y=x.right
    T2=y.left
    y.left=x
    x.right=T2
    x.height=max(findHeight(x.left), findHeight(x.right))+1
    y.height= max(findHeight(y.left),findHeight(y.right))+1
    return y

def rightRotation(root):
    x=root
    y=root.left
    T2=y.right
    x.left=T2
    y.right=x
    x.height=max(findHeight(x.left), findHeight(x.right))+1
    y.height= max(findHeight(y.left),findHeight(y.right))+1
    return y

def findHeight(root):
    if root==None:
        return 0
    return root.height

def CheckBalance(node):
    if node==None:
        return 0
    return findHeight(node.left) - findHeight(node.right)

def preOrder(node):
    if node==None:
        return
    print(node.value,' ',node.height , ' ', CheckBalance(node))
    preOrder(node.left)
    preOrder(node.right)

Root= Node(1)
Root=insert(Root,2)
preOrder(Root)
print('------')
Root=insert(Root,3)
preOrder(Root)
print('------')
Root=insert(Root,4)
preOrder(Root)
print('------')
Root=insert(Root,5)
preOrder(Root)
print('------')
Root=insert(Root,6)
preOrder(Root)
print('------')
Root=insert(Root,7)
preOrder(Root)
print('------')
Root=insert(Root,8)
preOrder(Root)

# In AVL tree the root node may change on insertion that's why we have to initialize 
# the root node on every insertion.
