from math import*
va=[5,3,7,8,14,9,12,6]
s,psum=0,0
for i in range(len(va)):
    v=va[i]
    s+=v
    s=s/len(va)
    psum+=v*v
    mse=sqrt(psum/len(va)-s*s)
print('均方差为：',round(mse,3))
