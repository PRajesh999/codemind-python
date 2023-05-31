a,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,a):
    if l[i]%k==0:
        c+=1
print(c)