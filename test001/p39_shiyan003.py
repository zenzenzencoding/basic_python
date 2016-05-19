#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月8日
描述：循环语句：1+2+...+99(非递归)
@author:ECNU_zenwan
'''
def mysum(a,b):
    s=0
    for i in range(a,b+1):
        s=s+i
    return s   
if __name__=='__main__':
    x=input("请输入起始数：")
    y=input("请输入结束数：")
    print "求和得："+repr(mysum(x,y))