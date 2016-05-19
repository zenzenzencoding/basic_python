#-*-coding:utf-8-*-
'''
Created on 2015年4月21日
Description：p153_2
@author:ECNU_zenwan
@version：
'''
h,m,s=raw_input("输入时间(H:M:S)").split(":")
h=int(h)
m=int(m)
s=int(s)
n=input("增加多少秒:")
s=s+n
if s>=60:
    m1=s//60
    s1=s%60
    s=s1
    m=m+m1
if m>=60:
    h1=m//60
    m1=m%60
    m=m1
    h=(h+h1)%24#控制时间早24小时内
print("增加%d秒后的时间是:%d:%02d:%02d")%(n,h,m,s)#保留2位整数