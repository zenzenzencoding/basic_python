def cal(n):
    a=1
    b=0
    c=0
    while a<=n+1:
        b=b+a
        c=c+b
        a=a+2
    return c
x=11
cal(x)
print("总和为:",cal(x))
