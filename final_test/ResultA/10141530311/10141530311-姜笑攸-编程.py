def cal(n):
    s1=0
    for i in range(1,n+1):
        s1+=2*i-1
    return s1

Sum=0
for j in range(1,7):
    Sum+=cal(j)
print("总和为:"+repr(Sum))
