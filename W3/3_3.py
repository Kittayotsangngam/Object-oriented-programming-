"""Chapter : 3 - item : 3 - Color_Crush
 ส่งมาแล้ว 3 ครั้ง
หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!" กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

    โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย



class Stack:

    def __init__(self):

    def push(self, value):

    def pop(self):

    def size(self):

    def isEmpty(self):



inp = input('Enter Input : ').split()

S = Stack()

### Enter Your Code Here ###

print(S.size())

### Enter Your Code Here ###"""
class Stack:

    def __init__(self,list = None) :
        if list== None :
            self.items = []
        else :
            self.items = list
    def push(self,i):
            self.items.append(i)
    def pop(self) :  
            return self.items.pop(len(self.items)-1)  
    def isEmpty(self) :
            return self.items==[]
    def size(self) :
            return len(self.items)


S=Stack()

inp = input('Enter Input : ').split()
count=0
countcombo =0
x=''
for i in inp:
    S.push(i)
    if i==x:
        count+=1
    else :
        x=i
        count=1
    if count==3:
        count=0
        for j in range(3):
            S.pop()
        countcombo+=1
        if S.size()>1:
            if S.items[-2] == S.items[-1] :
                x=S.items[-1]
                count = 2
            else :
                x=S.items[-1]
                count = 1
        elif S.size()==1:
                x=S.items[-1]
                count = 1
print(S.size())
for i in range(S.size()-1,-1,-1):
    print(S.items[i],end='')
if S.size()==0: print('Empty',end='')
if countcombo>=2:
    print('\nCombo : '+str(countcombo)+' ! ! !')

    
    


