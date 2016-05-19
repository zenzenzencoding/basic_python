def cal(n):
    m=int(n)
    i=0
    while m!=-1:
        i=i+m
        m=m-2
    return i
h=0
for x in range(1,12,2):
        h=h+int(cal(x))
print("总和为:",h)
