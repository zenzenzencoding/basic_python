﻿def intToBinArr( x ): 
    R=''
    while x!=0:
        temp = x % 2 #数字除以2的余数
        R = x // 2  #数字除以2的整数部分数
        R=temp+R
    return R
x=int(input('请输入一个正整数：'))
print( '转换为二进制的数据为：',intToBinArr(x)) 


