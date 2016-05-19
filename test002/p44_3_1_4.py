#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月8日
了解下变量的概念
@author:ECNU_zenwan
'''
def bl(a,b):
    print "a地址："+repr(id(a))
    print "b地址："+repr(id(b))
    if a<b:
        a,b=b,a #交换a，
    print "大数:"+repr(a)
    print "小数:"+repr(b)
    print "a新地址："+repr(id(a))
    print "b新地址："+repr(id(b))
if __name__=='__main__':
    m=input("please enter the first number:")
    n=input("please enter the second number:")
    bl(m, n)