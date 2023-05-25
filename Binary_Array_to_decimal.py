n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    n=n-1
    s+=i*2**n
print(s)