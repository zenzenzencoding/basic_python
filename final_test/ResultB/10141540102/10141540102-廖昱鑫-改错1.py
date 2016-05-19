L=[5,3,7,8,14,9,12,6]
v=0
m=0
for i in range(0,len(L)):
    v=v+float(L[i])
v=v/len(L)
for i in range(0,len(L)):
    m=float(L[i])*float(L[i])+m
m=m/len(L)
mse=m-v*v    
print('均方差为：%.3f',mse)

