#-*-coding:utf-8-*-
'''
Created on 2015��4��27��
Description:p158��1��
@author:ECNU_zenwan
@version: v1.0
'''
a,b,c,s,i=0,0,0,0,0
f=open(r"E:\document\�����ĵ�\ch5\�ı��ļ�\temperatures.txt") 
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
print("��������:%d\n��������:%d\n��������:%d\nƽ������:%.1f")%(a,b,c,s*1.0/i)