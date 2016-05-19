#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月10日
描述：谁是小偷？实际问题转化为数学问题，数学问题转化为程序设计语言
@author:ECNU_zenwan
'''
s1=s2=s3=s4=0
dictionary={'1':'a','2':'b','3':'c','4':'d'}
for x in range(1,5):
    if x!=1:
        s1=1
    if x==3:
        s2=1
    if x==4:
        s3=1
    if x!=4:
        s4=1
    if s1+s2+s3+s4==3:
        name=repr(x)
        print "小偷是"+(dictionary[name])#怎么去掉引号
        break
    