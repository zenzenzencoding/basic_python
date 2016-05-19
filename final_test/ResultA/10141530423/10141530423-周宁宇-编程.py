def cal(n):
    a=0
    L1=[]
    for i in range(0,n+1):
        a+=2*(i+1)-1
    L1.append(a)
    return L1
s=0
L1=cal(n)
for i in range(0,6):
    s=s+L1[i]
print('总和为:',s)
