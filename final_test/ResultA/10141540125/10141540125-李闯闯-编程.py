def cal(n):
    s(0)=1
for n in range(1,6):
    x=2*n+1
    s(n)=s(n-1)+x
return s(n)    
