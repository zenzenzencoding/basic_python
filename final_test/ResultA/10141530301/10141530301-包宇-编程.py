def cal(n):
    c=0
    for i in range(0,2*n):
        if i%2==1:
            c+=i
    return c
s=0
for j in range (1,7):
    s+=cal(j)
print(s)
    
