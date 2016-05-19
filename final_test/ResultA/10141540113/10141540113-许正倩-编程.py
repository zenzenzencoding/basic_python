def cal(n):
    s=0
    for i in range (1,2*n+1,2):
        s=s+i
    return s
sum=0
for n in range (1,7):
    sum=sum+cal(n)
print('总和为：',sum)
