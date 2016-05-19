def cal(n):
    a=len(n)
    sum=a*a
    return sum
l=[]
b=0
x=0
for i in range(1,7):
    b=2*i-1
    l.append(b)
    x+=cal(l)
print("总和为：",x)
    
