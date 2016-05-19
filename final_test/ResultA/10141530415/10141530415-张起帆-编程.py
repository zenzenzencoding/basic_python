def cal(n):
    si=0
    for i in range(1,n+1,2):
        si+=i
    return si
j=0
n=11
s=0
for j in range(1,n+1,2):
    s+=cal(j)
print(s)
