n = int(input("enter numbmer"))
list = []
for i in range (n):
    a = int(input())
    list.append(a)

pos=[]
neg=[]
for x in list:
    if x >= 0:
        pos.append(x)
    else:
        neg.append(x)


print("posi",pos)
print("negi",neg)

