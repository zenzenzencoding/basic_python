def cal(n):
    m=1
    t=2*n-1
    while t!=1:
        m+=t
        t-=2
    return m
s=0
for i in range(1,7):
    s+=int(cal(i))
print('总和为：',s)
        

