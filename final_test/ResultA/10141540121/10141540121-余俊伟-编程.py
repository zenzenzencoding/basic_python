def cal(n):
    r=0
    for i in range(0,n+1):
        r+=2*i+1
    return r
sum1=0
for i in range(0,6):
    sum1+=cal(i)
print('总和为:',sum1)
