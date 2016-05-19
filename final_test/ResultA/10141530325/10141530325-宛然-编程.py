def cal(n):
    b=n*n
    return b
s='(1)+(1+3)+(1+3+5)+(1+3+5+7+9)+(1+3+5+7+9)+(1+3+5+7+9+11)'
b=s.split(')+(')
a=0
for n in range(0,len(b)+1):
    a+=cal(n)
print('总和为:',a)
        
