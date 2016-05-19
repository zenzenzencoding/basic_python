#-*-coding:utf-8-*-
'''
Created on 2015年3月31日
Description：判断最大的数
@author:ECNU_zenwan
@version：V1.0
'''
a=input("输入第1个数：")
b=input("输入第2个数：")
c=input("输入第3个数：")
d=input("输入第4个数：")
max_number=a#初始化最大值为a
if max_number<b:
    max_number=b
if max_number<c:
    max_number=b
if max_number<d:
    max_number=d
print ("最大的数是：")+repr(max_number)#repr(obj):把obj对象转化为字符型
    