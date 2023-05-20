n=int(input())
a=list(map(int,input().split()))
sum=0
c=0
for i in range(0,n):
    sum+=a[i]
d=sum//n
for i in range(0,n):
    if(a[i]>=d):
        c+=1
print(c)