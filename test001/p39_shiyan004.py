#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月10日
描述：描述：循环语句：1+2+...+99(递归)
@author:ECNU_zenwan
'''
s=0
def f(start,n):
    if n==start:
        return start
    else: 
        return n+f(start,n-1)
if __name__=='__main__':
    start=input("输入起始值：start=")
    end=input("输入结束值：end=")
    print "result="+repr(f(start,end))