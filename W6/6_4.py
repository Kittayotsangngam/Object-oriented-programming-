"""Chapter : 6 - item : 4 - หอคอยแห่งฮานอย
 ส่งมาแล้ว 1 ครั้ง
เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
และให้ระวังเรื่องการสลับ list ให้ดีๆ

หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html

def move(n,A,B,C,maxn):
    #code here
n = int(input("Enter Input : "))"""
class Tower:
    def __init__(self, rod = 3):
        self.n = rod
        self.rods = [[]] * 3
        self.rods[0] = [i for i in range(rod, 0, -1)]
        self.rods[1] = []
        self.rods[2] = []

    def move(self, from_rod, to_rod):
        rodN = {"A":0,"B":1,"C":2}
        num = self.rods[rodN[from_rod]].pop()
        self.rods[rodN[to_rod]].append(num)
        print(self)

    def __str__(self, payload = None, rod = None, index = None):
        if rod == None:
            payload = ""
            rod = self.rods
            index = self.n
            try:
                payload += str(rod[0][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[1][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[2][index]) + "  " 
            except IndexError:
                payload += "|"
            
            payload += "\n"
            index -= 1
            return self.__str__(payload, rod, index)
        
        elif index >= 0:
            try:
                payload += str(rod[0][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[1][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[2][index]) + "  " 
            except IndexError:
                payload += "|"
            
            if index != 0:
                payload += "\n"
            index -= 1
            return self.__str__(payload, rod, index)
        
        else:
            return payload
         
def TowerOfHanoi(tower:Tower,n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"move 1 from  {from_rod} to {to_rod}")
        tower.move(from_rod,to_rod)
        return
    TowerOfHanoi(tower,n-1, from_rod, aux_rod, to_rod)
    print(f"move {n} from  {from_rod} to {to_rod}")
    tower.move(from_rod,to_rod)
    TowerOfHanoi(tower,n-1, aux_rod, to_rod, from_rod)
    

n = int(input("Enter Input : "))
tower = Tower(n)
print(tower)
TowerOfHanoi(tower,n, 'A', 'C', 'B')