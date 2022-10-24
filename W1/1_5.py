"""Chapter : 1 - item : 5 - vickrey auction
 ส่งมาแล้ว 1 ครั้ง
จงสร้าง vickrey auction แบบจำลอง
Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

word
"Enter All Bid : "
"not enough bidder"
"error : have more than one highest bid"
"winner bid is $ need to pay $"""
a= [int(x) for x in input("Enter All Bid : ").split()]
if len(a)<=1 :
    print("not enough bidder")
else:
    a.sort(reverse=True)
    if(a[1]==a[0]) : 
        print("error : have more than one highest bid")
    else :
        print("winner bid is",a[0],end=" ")
        print("need to pay",a[1])