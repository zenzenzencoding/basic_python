#-*-coding:utf-8-*-
'''
Created on 2015年5月19日
Description：002
@author:ECNU_zenwan
@version：
'''
while True:
    score=int(input("输入整数成绩(-1退出程序)："))
    if score==-1:
        break
    elif score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    else:
        grade="D"
    print score,"分为",grade,"级"
