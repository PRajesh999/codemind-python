q=int(input())
for j in range(0,q):
    n=input()
    s=0
    for i in n:
        if i.isdigit():
            s+=1

    if s>0:
        print("Yes")
    else:
        print("No")