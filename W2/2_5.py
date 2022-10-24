"""Chapter : 2 - item : 5 - ต่อคำหรรษา
 ส่งมาแล้ว 1 ครั้ง
ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

 
1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
จะไม่สามารถพูดว่า “Apple” ได้อีก


2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที


3. Ignore Case Sensitive


โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
- P < word > จะเป็นการต่อคำ
- R จะเป็นการเริ่มคำใหม่ทั้งหมด
- X เป็นการระบุว่าจบการทำงาน


โดยจะรับประกันว่า word ที่รับมา จะมีความยาวอย่างน้อยที่สุดคือ"""
print("*** TorKham HanSaa ***")
Arr = [a.split() for a in input("Enter Input : ").split(",")]
newArr=[]
firstWord = True
i=0
for W in Arr:
    if (W[0]=="P"):
        lastTwocap= W[1][-2] + W[1][-1]
        if(Arr[i+1][0]!='X' and Arr[i+1][0]!='R'):
            firstTwocap = Arr[i+1][1][0] + Arr[i+1][1][1]
        if(firstWord==True):
            newArr.append(W[1])
            firstWord = False
        print("'" + W[1]+"' -> ", end = "")
        print(newArr)
        if(Arr[i+1][0]!="X" and Arr[i+1][0]!="R"):
            if(lastTwocap.lower()==firstTwocap.lower()):
                newArr.append(Arr[i+1][1])
            else:
                print("'" + Arr[i+1][1]+"' -> game over")
                break
    elif (W[0]=="R"):
        newArr =[]
        firstWord =True
        print("game restarted")
    elif (W[0]=="X"):
        break
    else:
        print("'" + W[0] + " " + W[1]+"' is Invalid Input !!!")
        break
    i+=1
    firstTwocap =''
    lastTwocap =''