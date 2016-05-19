def cal(n):
    sum=0
    for i in range(n):
        sum+=2*i+1
    return (sum)
add=0
for j in range(1, 7):
    add+= cal(j)
print ('总和为:',add)

