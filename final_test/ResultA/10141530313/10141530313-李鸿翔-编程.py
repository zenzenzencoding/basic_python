def cal(n):
    m=0
    for i in range(0,n+1):
        h=i*2-1
        m=m+h
    print(m)
s=0
for j in range(1,7):
    s=s+cal(j)
print("总和为：",s)


