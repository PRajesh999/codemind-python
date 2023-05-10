n=int(input())
c=n*n
sum=0
while(c>0):
    r=c%10
    sum+=r
    c=c//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")