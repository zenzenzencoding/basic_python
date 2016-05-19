def cal(n):
    s=0
    for i in range(0,n):
        s=s+(1+2*i)
    return s
u=0
for i in range(1,7):
    u=u+cal(i)
print('总和为：',u)
