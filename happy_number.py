def happy(n):
    s=0
    while n!=0:
        r=n%10
        s+=pow(r,2)
        n=n//10
    return s
n=int(input())
while(1):
    if n==1 or n==7:
        print(True)
        break
    elif(n<10):
        print(False)
        break
    else:
        n=happy(n)
