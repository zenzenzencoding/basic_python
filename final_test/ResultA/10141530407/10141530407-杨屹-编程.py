def cal(n):
    for i in range(1,n+1):
        m=2*i-1
    return m
a=int(input('请输入n:'))
print(cal(a))

s=0
b=0
for j in range(1,7):
    s+=cal(j)
    b+=s
print(b)


