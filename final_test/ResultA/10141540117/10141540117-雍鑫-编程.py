def cal(n):
    s=0
    a=0
    for i in range(1,n+1):
        a=2*i-1
        s=s+a
    return s

sum=0
x=int(input('所求项数：'))
y=cal(x)
print('第%d项数为：'%x,y)
for i in range(1,x+1):
    sum=sum+cal(i)
print('总和为',sum)
