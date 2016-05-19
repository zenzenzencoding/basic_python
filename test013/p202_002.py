#-*-coding:utf-8-*-
'''
Created on 2015年5月26日
Description：
@author:ECNU_zenwan
@version：
'''
chr='输入出错!'
def funct(a,b,c):
    s=float(a+b)
    ave=s/2
    if c==0:
        print s
    elif c==1:
        print ave
    else:
        print chr
    
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
funct(a,b,c)