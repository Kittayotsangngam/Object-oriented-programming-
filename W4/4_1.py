"""Chapter : 4 - item : 1 - Basic Queue
 ส่งมาแล้ว 9 ครั้ง
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

                    หลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***"""
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

q=Queue()
x=input("Enter Input : ").split(',')
for i in range(len(x)):
    if(x[i][0]=='E'):
        q.enqueue(x[i].replace('E ',''))
        print("Add "+x[i].replace('E ','') + ' index is ' + str(q.size()-1))
    elif(x[i][0]=='D'):
        if(q.size()!=0):
            print("Pop "+q.front() + ' size in queue is ' + str(q.size()-1))
            q.dequeue()
        elif(q.size()==0):
            print('-1')
l=[]
if (q.size()!=0):
    print("Number in Queue is :  ",end='')
    print(q.tostring(),end ='')
elif (q.size()==0):
    print("Empty",end='')