#-*-coding:utf-8-*-
'''
Created on 2015��3��31��
Description������ĳ��ĳ��ĳ�£��ж�����һ�������
@author:ECNU_zenwan
@version��V1.0
'''
year=int(input("�����꣺"))
mon=int(input("�����£�"))
day=int(input("�����գ�"))
month_day={1:31,2:28,3:31,4:30,5:31,6:30,
           7:31,8:31,9:30,10:31,11:30,12:31}
if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))and(mon>2):
    day=day+1
for i in range(1,mon,1):
    day=day+month_day[i]
print ("����һ���еĵ�%d��,ôô��")%(day)