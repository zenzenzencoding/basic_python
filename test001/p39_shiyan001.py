#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月8日
描述：输出一个数的个位和十位的数字
思想：个位:x%10 十位:x/10%10 百位:x/100%10 千位:x/1000%10(移动小数点)
@author:ECNU_zenwan
'''
def qushu(a):
    if a in range(0,100):
        print "十位数："+repr(a//10)# //不管两者出现任何数，都以整除结果为准
        print "个位数："+repr(a%10)# 
    else:
        print "Error:输入的数字异常"
if __name__=='__main__':
    i=input("please enter a int number(0-100):")
    qushu(i)