import math
def cal(n):
    s=0
    for i in range(1,n):
        d=(i+(2*i-1)*i)/2
        s=s+d
        s=int(s)
    return s
x=7
print("总和为：",cal(x))
