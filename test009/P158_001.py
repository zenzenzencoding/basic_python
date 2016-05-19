#-*-coding:utf-8-*-
'''
Created on 2015年4月27日
Description:p158第1题
@author:ECNU_zenwan
@version: v1.0
'''
a,b,c,s,i=0,0,0,0,0
f=open(r"E:\document\助教文档\ch5\文本文件\temperatures.txt") 
while True:
    line=f.readline()
    if not line:break
    for item in line.split():
        item=int(item)
        s+=item
        i+=1
        if item>=85:a+=1
        if 85>item>=60:b+=1
        if item<60:c+=1
print("高温天数:%d\n舒适天数:%d\n寒冷天数:%d\n平均气温:%.1f")%(a,b,c,s*1.0/i)