def rev(n):
    rem=0
    while n:
        r=n%10
        rem+=r
        n=n//10
    return rem
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=rev(i)
print(s)