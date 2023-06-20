n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=list(map(int,input().split()))
    for j in range(1,a+1):
        if j in b:
            continue
        else:
            print(j)