n=int(input())
ce=0
co=0
while(n>0):
    r=n%10
    n=n//10
    if r%2==0:
        ce+=1
    else:
        co+=1
if ce>0 and co==0:
    print("Even")
elif co>0 and ce==0:
    print("Odd")
else:
    print("Mixed")