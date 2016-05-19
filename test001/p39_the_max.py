#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月10日
描述：输出三个数的最大者(迭代)
@author:ECNU_zenwan
'''
def maxnumber(a,b):
    if a>b:
        return a
    else:
        return b
if __name__=='__main__':
    x=input("输入第一个数：")
    y=input("输入第二个数：")
    z=input("输入第三个数：")
    return maxnumber(x, maxnumber(y, z))