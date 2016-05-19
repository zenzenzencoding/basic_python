#-*-coding:utf-8-*-
'''
Created on 2015年3月21日
Description：查表法
@author:ECNU_zenwan
@version：
'''
listdic={10:'A',9:'A',8:'B',7:'C',6:'D',5:'E',4:'E',3:'E',2:'E',1:'E',0:'E'}
def dengjihanshu(n):
    dengji=n//10
    return listdic[dengji]
x=input("输入成绩:")#2.7版本接受的是数字不是字符串，不需要类型转换
print ("成绩登记是"+dengjihanshu(x))
