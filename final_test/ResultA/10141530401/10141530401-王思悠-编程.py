def cal(n):
    s=0
    for i in range(1,n+1,2):
        s+=i
    return s
n=11
x=0
for i in range(1,n+1,2):
    x+=cal(i)
print("总和为:",x)
