def cal(n):
    s=0
    while n>2:
        m=n-2
        s=m+n
        n=m
    return s
n=int(input(''))
s=1
while n>2:
    s=s+cal(n)
    m=n-2
    n=m
print("总和为：",s)
