class BinaryTree:
    def __init__(self,value):                 
         self.value=value
         self.left=None
         self.right=None
    
    def insert(self,value):
        if self.value < value:
            if self.right:
                self.right.insert(value)
            else:
                self.right= BinaryTree(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left=BinaryTree(value)
    
    def deletion(self,value):
        def find_predecessor(root):
            if root.right ==None:
                root.right= root.left
                return root.value
            return find_predecessor(root.right)
            
        if self.isPresent(value)==None:
            print(value ,' Node is not present in the BST')
            return 
        print(self.value,' hello')
        if self.value > value:
                if self.left.value== value:
                    root=self.left
                    if root.left== None and root.right==None: #No child
                        print('root has no child')
                        self.left =None
                    elif root.left ==None : # root has one child : right child
                        self.left = root.right
                    elif root.right ==None: # root has one child : left child
                        self.left = root.left 
                    else:# root has 2 child
                        print('root has 2 child')
                        if root.left.right:
                            self.left.value = find_predecessor(root.left)
                        else:
                            root.value = root.left.value 
                            root.left = root.left.left
                else:
                    self.left.deletion(value)
        else:
            if self.right.value == value:
                    root=self.right
                    if root.left== None and root.right==None: #No child
                        print('root has no child')
                        self.right =None
                    elif root.left ==None : # root has one child : right child
                        self.right = root.right
                    elif root.right ==None: # root has one child : left child
                        self.right = root.left 
                    else:# root has 2 child
                        print('root has 2 child')
                        if root.left.right:
                            self.right.value = find_predecessor(root.left)
                        else:
                            root.value = root.left.value
                            root.left= root.left.left
                            
            else:
                self.right.deletion(value)
                
        

        

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.value,end=' ')
        if self.right:
            self.right.inOrderTraversal()

    def isPresent(self,value):
        if self.value == value:
            return True
        elif self.value > value and self.left :
            return self.left.isPresent(value)
        elif self.right:
            return self.right.isPresent(value)
        return False

    def get(self,value):
        if self.value == value:
            return self
        elif self.value > value and self.left :
            return self.left.get(value)
        elif self.right:
            return self.right.get(value)
        return False

    def LCA(self,A,B,available=0):
        if available==0:
            if self.isPresent(A)==True and self.isPresent(B)==True:
                return self.LCA(A,B,1)
            else:
                print('The given tree doesnot contain one of the node',A,B)
                return 

        if available==1:
                if self.value < A and self.value <B and self.left:
                    return self.right.LCA(A,B,1)
                elif self.value > A and self.value >B and self.right:
                    return self.left.LCA(A,B,1)
                else:
                    return self
    
    def distancebetween(self,A,B):
        root=self.LCA(A,B)
        if root is None:
            print('either ',A,' or ',B,' is not present in the BST')
            return
        return root.distance(A) -1 + root.distance(B) -1    

    def distance(self,A,h=0):
        if self.isPresent(A):
            if self is None:
                return 0
            if self.value == A:
                return h+1
            if self.value > A :
                return self.left.distance(A,h+1)
            else:
                return self.right.distance(A,h+1)
        else:
            print(A, ' is not present in the tree')

    def LevelWiseprint(self,queue):
            if len(queue)==0:
                return
            root= queue.pop(0)
            if root:
                print(root.value,end=' ')
                queue.append(root.left)
                queue.append(root.right)
            else:
                print(None,end=' ')
            self.LevelWiseprint(queue)
            
    
    def height(self):
        if self is None:
            return 0
        left=0
        right=0
        if self.left:
            left= self.left.height()
        if self.right:
            right=self.right.height()
        return max(left,right)+1


BT = BinaryTree(12)
BT.insert(10)
BT.insert(50)
BT.insert(70)
BT.insert(60)
BT.insert(25)
BT.insert(20)
BT.insert(40)
BT.insert(15)
BT.insert(30)
BT.insert(48)
BT.insert(13)
BT.insert(18)
BT.insert(28)
BT.insert(47)
BT.insert(14)
BT.insert(17)
BT.insert(46)
# BT.inOrderTraversal()
print()
# lca=BT.LCA(3,11)
# if lca:
# print(lca.value)

BT.LevelWiseprint([BT])
print()
print('height of the tree: ',BT.height())
# print(BT.distance(3))
# print(BT.distancebetween(2,6))
# print(BT.get(4).value)
#deletion and distance
# BT.deletion(3)
print(BT.diameter())
# BT.LevelWiseprint([BT])