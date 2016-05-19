#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月8日
描述：条件分支语句
@author:ECNU_zenwan
'''
a=input("请输入一个数：")
if a>0 and a-int(a)==0:
    print "有效数"
elif a in range(1,100):#默认步长为1，注意和1<=a<100的区别
    print "合理数"
else:
    print "无效数"