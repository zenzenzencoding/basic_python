#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月8日
描述：最大公约数(更相减损数)
思想：两个数的最大公约数就是除数和余数的最大公约数
@author:ECNU_zenwan
'''
def gxjss(a,b):
    if a<b:
        a,b=b,a #等价于temp=a a=b b=temp
    if (a==b):
        return b
    else:
        return gxjss(b,a-b)
if __name__=='__main__':
    m=input("please enter the first number:")
    n=input("please enter the second number:")
    print "最大公约数是"+repr(gxjss(m,n))
    