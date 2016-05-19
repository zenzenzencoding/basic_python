#-*-coding:utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月17日
description：求三角形面积
@author:ECNU_zenwan
@version: v1.0
'''
import math
def area(a,b,c):
    q=(a+b+c)/2
    s=math.sqrt(q*(q-a)*(q-b)*(q-c))
    return s
if __name__=='__main__':
    x=input("please enter the first side length:")
    y=input("please enter the second side length:")
    z=input("please enter the third side length:")
    print"the area is:"+repr(area(x, y, z))
    