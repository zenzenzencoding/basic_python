def cal(n):
    s=0
    x=0
    for i in range(1,n+1):
        x=0
        for j in range(1,2*i,2):
            x+=j
        s+=x
    return s
n=6
print('总和为:',cal(n))
