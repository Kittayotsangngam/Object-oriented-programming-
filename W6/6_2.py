"""Chapter : 6 - item : 2 - Length of a String EXTRA
 ส่งมาแล้ว 1 ครั้ง
ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

def length(txt):     
    #Code Here
print("\n",length(input("Enter Input : ")),sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)"""
def length(txt):
    global i
    if txt == '' :
        return 0
    else :
        if(i==0):
            print(txt[0],end='*')
            i=1
        else:
            print(txt[0],end='~')
            i=0
        return 1+length(txt[1:])
inp = input("Enter Input : ")
i=0