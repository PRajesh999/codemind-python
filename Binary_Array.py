n=int(input())
a=list(map(int,input().split()))
flag=0
for i in range(0,n):
    if(a[i]!=1 and a[i]!=0):
       flag=1
       break
if flag==1:
     print(False)
else:
     print(True)