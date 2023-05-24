def prime(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    if c==1:
        return False
    else:
        return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and prime(i):
        c+=1
print(c)