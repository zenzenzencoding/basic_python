#-*-coding:utf-8-*-
'''
Created on 2015年3月31日
Description：输入某年某年某月，判断是这一年的哪天
@author:ECNU_zenwan
@version：V1.0
'''
year=int(input("输入年："))
mon=int(input("输入月："))
day=int(input("输入日："))
month_day={1:31,2:28,3:31,4:30,5:31,6:30,
           7:31,8:31,9:30,10:31,11:30,12:31}
if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))and(mon>2):
    day=day+1
for i in range(1,mon,1):
    day=day+month_day[i]
print ("它是一年中的第%d天,么么哒")%(day)