def cal(n):
    y=0
    for i in range(1,n+1):
        for j in range(0,2*i-1):
            y=y+2*i-1
    return y
n1=6
s=cal(n1)
print(s)
