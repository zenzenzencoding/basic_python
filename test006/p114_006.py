#-*-coding:utf-8-*-
'''
Created on 2015年4月7日
Description：第六题
@author:ECNU_zenwan
@version：
'''
#算法一
''' 
string=raw_input("输入字符串:")
while string !='quit':
    print ("你输入的字符串长度为%d"%(len(string)))
    string=raw_input("输入字符串")
    
'''
#优化算法
while True:
    string=raw_input("输入字符串:")
    if string =='quit':break
    print ("你输入的字符串长度为%d"%(len(string)))

    
