"""Chapter : 3 - item : 1 - รู้จักกับ STACK
 ส่งมาแล้ว 3 ครั้ง
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty"""
x=input("Enter Input : ").split(',')
stack =[]
countSize = 0

for i in range(len(x)):
    if(x[i][0]=='A'):
        stack.append(x[i].replace('A ',''))
        countSize+=1
        print("Add = "+x[i].replace('A ','') + ' and Size = ' + str(countSize))
    elif(x[i][0]=='P'):
        if(countSize!=0):
            countSize-=1
            print("Pop = "+stack[-1] + ' and Index = ' + str(countSize))
            stack.pop()
        elif(countSize==0):
            print('-1')
if (len(stack)!=0):
    print("Value in Stack = ",end='')
    for j in range(len(stack)):
        print(stack[j],end=' ')
elif (len(stack)==0):
    print("Value in Stack = Empty",end='')