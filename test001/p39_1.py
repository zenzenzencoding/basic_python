# -*-coding: utf-8-*-
'''
Created on 2015��3��8��
������ֱ�������Լ������
@author: ECNU_zenwan
'''
a=input("please enter the first number:")
b=input("please enter the second number:")
if a<b:
    #a,b=b,a
    temp=a
    a=b
    b=temp
for i in range(b,0,-1):
    if a%i==0 and b%i==0:
        print i
        break