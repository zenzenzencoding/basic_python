def cal(n):
    _sum=0
    for i in n:
        _sum+=i
    return _sum
s=0
for j in range(1,13,2):
    n=list(range(1,j+2,2))
    s+=cal(n)
print('总和为:',s)
    
