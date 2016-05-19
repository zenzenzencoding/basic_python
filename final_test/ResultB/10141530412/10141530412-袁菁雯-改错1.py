import math
va=[5,3,7,8,14,9,12,6]
s,psum=0,0
for i in range(len(va)):
    v=va[i]
    s+=v
    psum+=v**2
    s/=len(va)
    mse=math.sqrt(float(psum)/len(va)-s**2)
print('均方差为：',mse)
