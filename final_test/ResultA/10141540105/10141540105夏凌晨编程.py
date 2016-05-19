def cal(n):
    everysum=0
    for i in range(1,n+1):
        everysum=everysum+2*i-1
    return everysum
sum=0
x=6
for j in range(1,x+1):
    sum=sum+int(cal(j))
print(sum)
