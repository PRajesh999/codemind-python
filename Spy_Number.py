c=int(input())
sum=0
prod=1
while(c>0):
    r=c%10
    sum+=r
    prod*=r
    c=c//10
if(sum==prod):
    print("Spy Number")
else:
    print("Not Spy Number")