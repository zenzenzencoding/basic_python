#-*-coding:utf-8-*-
'''
Created on 2015年4月28日
Description：p158第2题
@author:ECNU_zenwan
@version：1.0
'''
from datetime import datetime
f1=open(r"E:\document\助教文档\ch5\文本文件\customer.txt")
now = datetime.now() #获取系统当前日期的年
gender= dict({1:'男',2:'女'})
new_file=[]
#print now.year
while True:
    line=f1.readline()
    if not line:break
    id=line.split()
    years=int(id[1][6:10])#该customer的出生年份
    mon = int(id[1][10:12])#该customer的出生月份
    da = int(id[1][12:14])#该customer的出生日
    age = now.year- years#注意实足年龄的算法，未过生日的话还要减1
    if now.month < mon:
        age -= 1
    elif now.month == mon:
        if now.day < da:
            age -= 1
    if int(id[1][16]) % 2 == 0:#计算男女
        key = 2
    else :
        key = 1
    new_file.append([id[0],gender[key],age])
f2 = open(r"E:\document\助教文档\ch5\文本文件\cusinfo.txt",'w')
for item in new_file:
    f2.write('%s\t%s\t%d\n'%(item[0],item[1],item[2]))
f1.close()
f2.close()
