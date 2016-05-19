def cal(n):
    s=0
    b=int((n+1)/2)
    m=1
    for i in range(0,b):
        s=s+m
        m+=2
    return s
x=0
for j in range(1,12,2):
    x+=cal(j)
print(x)
    
    
        
