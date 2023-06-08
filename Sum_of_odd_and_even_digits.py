n=int(input())
l=list(map(int,input().split()))
c1=0
c2=0
for i in range(0,n):
    if i==0 or i%2==0:
        c1+=l[i]
    else:
        c2+=l[i]
if c1-c2==0:
    print("YES")
else:
    print("NO")