def cal(n):
    s=0
    for i in range(1,2*n,2):
        s=s+i
    return s
c=0
for j in range(1,7):
    c=c+cal(j)
print('总和为:',c)
