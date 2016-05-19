def cal(n):
    a=0
    for i in range(1,n+1,2):
        a=a+i
    return(a)
n=11
s=0
for i in range(1,n+1,2):
    s=s+cal(i)
print('总和为：%4d'%s)
