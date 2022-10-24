"""Chapter : 7 - item : 2 - หาค่า Below
 ส่งมาแล้ว 6 ครั้ง
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()"""
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
        self.s=''

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
        if node :
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def printNode(self,min,mini):
        if min :
            self.printNode(min.left,mini)
            if(min.data<mini):
                self.s+=str(min.data)
                self.s+=(' ')
            self.printNode(min.right,mini)
        return self.s

T = BST()
inp = input('Enter Input : ').split('|')
inp[0]=inp[0].split(' ')
for i in inp[0]:
    root = T.insert(int(i))
T.printTree(root)
print("--------------------------------------------------")
print('Below '+inp[1]+' :',end=' ')
print(T.printNode(root,int(inp[1])),end='')
if(len(T.s)==0):
    print('Not have')