"""Chapter : 7 - item : 4 - สนุกไปกับ Binary Search Tree
 ส่งมาแล้ว 1 ครั้ง
ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class Queue:
    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.size() == 0

    def enQ(self, data):
        self.item.append(data)

    def deQ(self):
        return self.item.pop(0)
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
    def printTree_1(self, node):
        if node != None:
            print(node,end=' ')
            self.printTree_1(node.left)
            self.printTree_1(node.right)
    def printTree_2(self, node):
        if node != None:
            self.printTree_2(node.left)
            print(node,end=' ')
            self.printTree_2(node.right)
    def printTree_3(self, node):
        if node != None:
            self.printTree_3(node.left)
            self.printTree_3(node.right)
            print(node,end=' ')
    def printTree_4(self, s):
        storeNode = Queue()
        storeNode.enQ(self.root)
        while not storeNode.isEmpty():
            popNode = storeNode.deQ()
            print(popNode, '', end='')
            if popNode.left is not None:
                storeNode.enQ(popNode.left)
            if popNode.right is not None:
                storeNode.enQ(popNode.right)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print('Preorder : ',end='')
T.printTree_1(root)
print('\nInorder : ',end='')
T.printTree_2(root)
print('\nPostorder : ',end='')
T.printTree_3(root)
print('\nBreadth : ',end='')
T.printTree_4(root)