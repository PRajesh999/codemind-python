l=[]
for i in range(int(input())):
    b=int(input())
    l.append(b)
a=int(input())
s=0
for i in l:
    if i<=a:
        s+=1
    else:
        s+=2
print(s)