"""Chapter : 2 - item : 3 - New Range
 ส่งมาแล้ว 2 ครั้ง
ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function

ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1

ถ้าหากเป็น 2 argument -> range(a, b)        | start = a , end = b , step = 1

ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = c"""
def new_range(input):
    ans=[]
    if len(input)==1:
        temp=0.0
        while temp<input[0]:
            ans.append(temp)
            temp+=1
    elif len(input)==2:
        temp=input[0]
        while temp<input[1]:
            ans.append(temp)
            temp+=1
    elif len(input)==3:
        temp=input[0]
        while temp<input[1]:
            ans.append(temp)
            temp+=input[2]
    return ans

print("*** New Range ***")
input=[float(i) for i in input ("Enter Input : ").split(" ")]
answer = new_range(input)
for i in range(len(answer)):
    answer[i]=float("{:.3f}".format(answer[i]))
print(tuple(answer))
