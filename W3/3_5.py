"""Chapter : 3 - item : 5 - แปลงเลขฐาน 10 เป็น เลขฐาน 2 ด้วย STACK
 ส่งมาแล้ว 2 ครั้ง
จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง

class Stack :

    ### Enter Your Code Here ###

def dec2bin(decnum):

    s = Stack()

    ### Enter Your Code Here ###

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))"""
class Stack :

    def __init__(self):
        self.new =0
        self.dec =0
        self.y =[]
    def detobi(self,dec):
        self.dec = dec
        while(self.dec !=0):
            self.new =self.dec%2
            self.y.append(self.new)
            self.dec = self.dec//2
        return self.y



def dec2bin(decnum):
    s = Stack()
    x=s.detobi(decnum)
    a=""
    for i in range(len(x)):
        a+= str(x.pop())
    return a

    

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))