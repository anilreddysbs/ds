#Binary tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,v):
        newnode=node(v)
        if self.root==None:
            self.root=newnode
        else:
            self.insert(self.root,newnode)
    def insert(self,root,newnode):
        print("0.Left 1.Right:",end="")
        x=int(input())
        if x==0:
            if root.left==None:
                root.left=newnode
            else:
                self.insert(root.left,newnode)
        else:
            if root.right==None:
                root.right=newnode
            else:
                self.insert(root.right,newnode)
    def display(self):
        print("1.preorder 2.inorder 3.postorder",end="")
        ch=int(input())
        if ch==1:
            self.preorder(self.root)
        elif ch==2:
            self.inorder(self.root)
        else:
            self.postorder(self.root)
        print()
    def inorder(self,root):
        if root!=None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root!=None:
            print(root.data,end=" ")
            self.inorder(root.left)
            self.inorder(root.right)
    def postorder(self,root):
        if root!=None:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end=" ")
t=tree()
op=1
while op!=0:
    print("1.insert 2.display:",end="")
    op=int(input())
    if op==1:
        v=int(input("Enter value:"))
        t.create(v)
    if op==2:
        t.display()
            
