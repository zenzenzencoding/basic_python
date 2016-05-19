#-*-coding:utf-8-*-
'''
Created on 2015年4月21日
Description：
@author:ECNU_zenwan
@version：
'''
h,m,s=raw_input("输入时间(H:M:S)").split(":")
h2,m2,s2=raw_input("输入增加时间(H:M:S)").split(":")
h=int(h)+int(h2)
m=int(m)+int(m2)
s=int(s)+int(s2)
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
print("增加%2d:%02d:%02d秒后的时间是:%02d:%02d:%02d")%(int(h2),int(m2),int(s2),h,m,s)#保留2位整数