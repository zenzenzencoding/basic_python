#-*-coding:utf-8-*-
'''
Created on 2015��5��26��
Description��
@author:ECNU_zenwan
@version��
'''
#1
def aver1(a,b):
    d=float((a+b))/2
    return d
a=int(input("a="))
b=int(input("b="))
print ("average",aver1(a,b))
#2
def aver2(a,b):
    global d
    d=(a+b)/2
    return d
x1=input("a=")
x2=input("b=")
print("average=",d)