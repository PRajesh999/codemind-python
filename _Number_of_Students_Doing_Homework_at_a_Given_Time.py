n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
o=int(input())
c=0
for i in range(0,n):
    if(o>=l1[i] and o<=l2[i]):
        c+=1
print(c)