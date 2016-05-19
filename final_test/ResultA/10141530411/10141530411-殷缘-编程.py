def cal(n):
    an=0
    for i in range(1,2*n+1,2):
        an+=i
    return an
s=0
for i in range(1,7):
    s+=cal(i)
print('总和为: ',s)
