a=int(input())
flag=0
for i in range(0,a):
    s=int(a**0.5)
    sq=s*s
    if sq==a:
    	flag=1
if flag==1:
    print(True)
else:
    print(False) 