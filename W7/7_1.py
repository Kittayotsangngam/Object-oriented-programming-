"""ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        p=Node(data)
        if self.root ==None:
            self.root=p
            return self.root
        elif(p.data>self.root.data):
            p=Node(data)
            t=self.root
            while(True):
                if(t.data<p.data):
                    if(t.right==None):
                        t.right=p
                        return self.root
                    t=t.right
                else:
                    if(t.left==None):
                        t.left=p
                        return self.root
                    t=t.left
        elif(p.data<self.root.data):
            p=Node(data)
            t=self.root
            while(True):
                if(t.data<p.data):
                    if(t.right==None):
                        t.right=p
                        return self.root
                    t=t.right
                else:
                    if(t.left==None):
                        t.left=p
                        return self.root
                    t=t.left
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)