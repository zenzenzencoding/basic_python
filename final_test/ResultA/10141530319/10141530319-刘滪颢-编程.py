def cal(n):
    t=(1+n)*((n+1)/2)/2
    return t
s=0
for n in range(1,12,2):
    s+=cal(n)
print('总和为:',int(s))

