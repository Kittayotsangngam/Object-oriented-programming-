"""Chapter : 4 - item : 3 - code with queue
 ส่งมาแล้ว 2 ครั้ง
รับ string มาเข้าคิวหา secret code โดยรับ input คือ

code เป็น string ยาว

hint คือตัวแรกของรหัสที่ถูกต้อง



**คำใบ้**

ascii ของ "f" มีค่า = 102

ascii ของ "g" มีค่า = 103

ascii ของ "h" มีค่า = 104

ascii ของ "i" มีค่า = 105

ascii ของ "j" มีค่า = 106"""
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
x=input('Enter code,hint : ').split(',')
q=Queue()
for i in range(len(x[0])):
    q.enqueue(chr((ord(x[0][i]))+(ord(x[1])-ord(x[0][0]))))
    print(q.tostring())
    