"""Chapter : 6 - item : 3 - POWER!
 ส่งมาแล้ว 1 ครั้ง
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab  """
def power(a,b):
    a=int(a)
    b=int(b)
    if(b==0):
        return 1
    elif(b>1):
        a=a*temp
        return power(a,b-1)
    elif(b==1):
        return a

inp=input('Enter Input a b : ').split(' ')
temp=int(inp[0])
print(power(inp[0],inp[1]))