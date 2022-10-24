"""Chapter : 6 - item : 5 - วาดภาพแสนสุข
 ส่งมาแล้ว 3 ครั้ง
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def staircase(n):
    #code here

print(staircase(int(input("Enter Input : "))))"""
def staircase(n,i):
    if n==0:
        return 'Not Draw!'
    elif(n>=1):
        staircase(n-1,i+1)
        print("_"*(i),end='')
        print("#"*(n))
        return ''
    elif(n<=1):
        staircase(n+1,i+1)
        print("_"*(abs(n)-1),end='')
        print("#"*(i+1))
        return ''
print(staircase(int(input("Enter Input : ")),0))