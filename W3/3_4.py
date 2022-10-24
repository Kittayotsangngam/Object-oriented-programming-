"""Chapter : 3 - item : 4 - Into the Woods
 ส่งมาแล้ว 1 ครั้ง
กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :   A  <Heights>  แสดงถึงความสูงของต้นไม้  ,   B  คือการหันหลังกลับมามอง

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

class Stack:

    ### Enter Your Code Here ###

S = Stack()


inp = input('Enter Input : ').split(',')

### Enter Your Code Here ###"""
class Stack:

    def __init__(self):
        self.items = []
        self.ip=[]
        self.tr=[]
        self.count=0
        self.temp=0
    def value(self, value):
        self.value = value
        for i in range(len(self.value)):
            self.ip = self.value[i].split()
            if(self.ip[0]=="A"):
                self.tr.append(int(self.ip[1]))
            else:
                self.B()
    def B(self):
        for i in reversed(range(len(self.tr))):
            if(self.temp<self.tr[i]):
                self.temp=self.tr[i]
                self.count+=1
        print(self.count)
        self.temp=0
        self.count=0
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    
S = Stack()


inp = input('Enter Input : ').split(',')

S.value(inp)
