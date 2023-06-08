n=int(input())
l=list(map(int,input().split()))
key=int(input())
for i in range(0,n):
    if l[i]==key:
        print(i)
        break
else:
    print(-1)