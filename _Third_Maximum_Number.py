n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(l[-1])
elif n==2:
    print(max(l))
else:
    a=list(set(l))
    a.sort()
    print(a[-3])