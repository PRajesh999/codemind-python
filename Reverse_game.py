def rev(n):
    rem=0
    while n:
        r=n%10
        rem=rem*10+r
        n=n//10
    return rem
n=int(input())
l=list(map(int,input().split()))
for i in l:
    s=rev(i)
    print(s,end=" ")