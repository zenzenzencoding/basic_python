#-*-coding:utf-8-*-
'''
Created on 2015��4��21��
Description��p153_2
@author:ECNU_zenwan
@version��
'''
h,m,s=raw_input("����ʱ��(H:M:S)").split(":")
h=int(h)
m=int(m)
s=int(s)
n=input("���Ӷ�����:")
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
    h=(h+h1)%24#����ʱ����24Сʱ��
print("����%d����ʱ����:%d:%02d:%02d")%(n,h,m,s)#����2λ����