def cal(n):
    sum=0
    for i in range(1,n+1,1):
      
            for j in range(1,2*i,2):
                while i>0:
                    sum+=j*i
                    i=i-1
    return sum
print(cal(6))
                
