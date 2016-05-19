import math
va=[5,3,7,8,14,9,12,6]
s,psum=0,0
for i in range(len(va)):
    v=va[i]
    s+=v
    psum+=v*v
s/=len(va)
from math import sqrt
mse=sqrt(psum/len(va)-s*s)
print('均方差为：%.3f'%mse)
