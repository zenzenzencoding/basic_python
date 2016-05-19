sum=0
n=1
while n!=13:
    def cal(n):
        s=0
        for i in range(1,n+1,2):
            s+=i
        return s
    sum+=cal(n)
    n+=2
print('总和为:',sum)
        
        
