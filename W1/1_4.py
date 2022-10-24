"""Chapter : 1 - item : 4 - สนุกไปกับการวาดรูป (2)
 ส่งมาแล้ว 1 ครั้ง
เขียนภาษา Python เพื่อวาดพีระมิด ซึ่งจะรับ input เป็นขนาดของพีระมิด โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป"""
print("*** Fun with Drawing ***")
a=int(input("Enter input : "))
z=(1+(a-1)*4)
m=z/2
for i in range(z):
    for j in range(z):
        t= i%2==0 and j>=i and j<=z-i-1 and i<m
        d= i%2==0 and i>=j and j>=z-i-1 and i>m
        l= j%2==0 and j<=i and i<=z-j-1 and j<m
        r= j%2==0 and i<=j and i>=z-j-1 and j>m
        if t or d or l or r:
            print("#",end= "")
        else : 
            print(".",end= "")
    print("")