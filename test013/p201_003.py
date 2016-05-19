#-*-coding:utf-8-*-
'''
Created on 2015年5月27日
Description：
@author:ECNU_zenwan
@version：
'''
s1=0
n=input("输入n:")
for i in range(1,n+1):
    jc=1
    for j in range(1,i+1):
        jc=jc*j
    s1=s1+jc
print s1
