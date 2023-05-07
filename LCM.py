n,m=map(int,input().split())
i=0
while(1):
    i+=1
    if n*i%m==0:
        break
print(n*i)