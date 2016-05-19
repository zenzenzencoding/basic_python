def cal(n):
    t=2*n-1
    an=(1+t)*n/2
    return an
s=0
k=11
c=int((k+1)/2)
for i in range(1,c+1):
    b=cal(i)
    s=s+int(b)
print('总和为:',s)
            
        
