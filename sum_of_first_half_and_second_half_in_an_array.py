n=int(input())
l=list(map(int,input().split()))
sum1=0
sum2=0
a=int(n/2)
for i in range(0,a):
    sum1+=l[i]
for i in range(a,n):
    sum2+=l[i]
print(sum1)
print(sum2)