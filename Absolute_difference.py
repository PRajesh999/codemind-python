def prime(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
f=1
g=1
for i in l:
    if prime(i):
        f*=i
    else:
        g*=i
print(abs(f-g))