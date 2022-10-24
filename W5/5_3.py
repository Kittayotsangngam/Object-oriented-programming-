"""Chapter : 5 - item : 3 - รวม Linked List
 ส่งมาแล้ว 5 ครั้ง
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p
    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.previous = p 
            self.head = p

    def insert(self, pos, item):
        p = Node(item)
        c = self.size()
        if self.isEmpty():
            self.head = p
            self.tail = p
        elif pos == 0 or -1*pos>c:
            self.head.previous=p
            p.next = self.head
            self.head = p

        elif pos>=c-1:
            self.tail.next = p
            p.previous = self.tail
            self.tail =p
        elif pos>0:
            t=self.head
            i=0
            while i<pos -1:
                i+=1
                t=t.next
            p.next=t.next
            t.next.previous = p
            t.next = p
            p.previous = t
        else :
            t=self.tail
            i=1
            while i<-1*pos:
                i+=1
                t=t.previous
            p.previous = t.previous
            t.previous.next = p
            t.previous = p
            p.next = t

                
        

    def search(self, item):
        t = self.head
        while t!=None:
            if t.value==item:
                return "Found"
            t=t.next
        return "Not Found"

    def index(self, item):
        t = self.head
        i = 0
        while t!=None:
            if t.value==item:
                return i
            i+=1
            t=t.next
        return -1
    def it(self,j):
        t = self.head
        i = 0
        while t!=None:
            if i==int(j):
                print(t)
                return t
            i+=1
            t=t.next
        return -1


    def size(self):
        s=0
        t=self.head
        while t!=None:
            s+=1
            t=t.next
        return s

    def pop(self):
        out = self.tail.value
        self.tail = self.tail.previous
        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None
        return out

        
inp = input('Enter Input (L1,L2) : ').split(' ')
ll1=LinkedList()
ll2=LinkedList()
ll3=LinkedList()
inp[0]=inp[0].split('->')
inp[1]=inp[1].split('->')
for i in inp[0]:
    ll1.append(i)
for i in inp[1]:
    ll2.append(i)
print('L1    : '+ll1.__str__())
print('L2    : '+ll2.__str__())
for i in range(ll2.size()-1,-1,-1):
    ll1.append(ll2.pop())
print('Merge : '+ll1.__str__())
