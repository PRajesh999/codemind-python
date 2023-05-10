n=int(input())
q=n
prod=1
sum=0
while(q!=0):
    r=q%10
    for i in range(1,r+1):
      prod*=i  
    sum+=prod
    prod=1
    q=q//10
if(sum==n):
    print("The number {} is a strong number".format(n))
else:
    print("The number {} is not a strong number".format(n))