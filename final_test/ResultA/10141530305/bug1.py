x=int(input('请输入一个正整数：'))
def intToBinArr( x ): 
    R=float(input(''))
    while x==0:
        temp = x % 2 #数字除以2的余数
        x = x // 2  #数字除以2的整数部分数
        R+=int(str(temp))
    return R
print( '转换为二进制的数据为：',R) 


