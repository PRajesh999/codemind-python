def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
while n!=0:
    a=int(input())
    f=fact(a)
    print(f)
    n-=1