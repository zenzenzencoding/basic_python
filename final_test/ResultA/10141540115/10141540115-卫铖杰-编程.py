def cal(n):
    c=0
    for a in range(1,n+1,2):
        c=c+a
    return c
#主程序
x=11
s=0
for i in range(1,x+1,2):
    s=s+cal(i)
print('总和为:',s)
