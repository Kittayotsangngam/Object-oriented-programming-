"""Chapter : 6 - item : 1 - Fibonacci
 ส่งมาแล้ว 1 ครั้ง
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

หาลำดับ Fibonacci ของ input ที่รับเข้ามาโดยใช้ Recursive"""
def fibo(n):
    if n <= 1:
       return n
    else:
       return(fibo(n-1) + fibo(n-2))
inp=input('Enter Number : ')
print('fibo(' +inp+ ') = '+str(fibo(int(inp))))