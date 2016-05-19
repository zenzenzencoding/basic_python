def cal(n):
    x=0
    for i in range(1,n+1):
        x=x+2*i-1
    return (x)
s=0
for i in range(1,7):
    s=s+cal(i)
print('总和为:',s)
