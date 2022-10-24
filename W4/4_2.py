"""Chapter : 4 - item : 2 - แถวคอย
 ส่งมาแล้ว 2 ครั้ง
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

"""
class Queue:
    def __init__(self, l=None):
        if l != None:
            self.items = l
        else:
            self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def front(self):
        return self.items[0]
    def tostring(self):
        return self.items
x=input('Enter people and time : ').split(' ')
q=Queue()
qOne=Queue()
qTwo=Queue()
countqOne=0
countqTwo=0
for i in range(len(x[0])):
    q.enqueue(x[0][i])
for j in range(int(x[1])):
    print(j+1,end=' ')
    if(countqOne==3 and qOne.size()>0):
        qOne.dequeue()
        countqOne=0
    if(countqTwo==2 and qTwo.size()>0):
        qTwo.dequeue()
        countqTwo=0
    if(q.size()>0 ):
        if(qOne.size()<5):
            qOne.enqueue(q.front())
            q.dequeue()
        else :
            qTwo.enqueue(q.front())
            q.dequeue()
    print(q.tostring(),end=' ')
    print(qOne.tostring(),end=' ')
    print(qTwo.tostring())
    if(qOne.size()>0):
        countqOne+=1
    if(qTwo.size()>0):
        countqTwo+=1