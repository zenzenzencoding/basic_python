#-*-coding:utf-8-*-
'''
Created on 2015��5��26��
Description��
@author:ECNU_zenwan
@version��
'''
def watermelon(d):
    day=0
    x1=int(d)
    while x1>0:
        x2=x1-(int(x1/2)+2)
        x1=x2
        day+=1
    return day
x=input("x=")
while int(x) in (range(2000)):
    print "days:",watermelon(x)
    x=input("x=")
        
    