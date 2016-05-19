#-*-coding:utf-8-*-
'''
Created on 2015年5月12日
Description：编程打印如下星号，必须使用循环语句
@author:ECNU_zenwan
@version：
'''
n=input("输入n:")
i=0
for i in range(n):
    j=i
    if i<=(n/2):
        print ' '*((n-(i*2+1))/2),
        print '*'*(2*i+1)
    else:
        i=n-i
        print ' '*((n-(i*2+1))/2),
        print '*'*(2*i+1)
    
    
        