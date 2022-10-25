inp=input("Enter Input : ").split('/')
inp[0]=inp[0].split(' ')
inp[1]=inp[1].split(',')
sum=0
for i in inp[0]:
    sum+=int(i)
print(sum)
def traverse(root):
    global summa
    summa += int(inp[0][root])

    left_node = 2*root+1
    right_node = 2*root+2
    if left_node < len(inp[0]):
        traverse(2*root+1)
    if right_node < len(inp[0]):
        traverse(2*root+2)

for compare in inp[1]: 
    Pow1 = 0
    Pow2 = 0

    compare=compare.split(' ')
    index1 = int(compare[0])
    index2 = int(compare[1])

    summa = 0
    traverse(index1)
    Pow1 = summa

    summa = 0
    traverse(index2)
    Pow2 = summa

    if Pow1 > Pow2:
        print(str(index1)+'>'+str(index2))
    elif Pow1 < Pow2:
        print(str(index1)+'<'+str(index2))
    elif Pow1 == Pow2:
        print(str(index1)+'='+str(index2))