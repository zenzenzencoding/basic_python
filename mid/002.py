#-*-coding:utf-8-*-
'''
Created on 2015��5��19��
Description��002
@author:ECNU_zenwan
@version��
'''
while True:
    score=int(input("���������ɼ�(-1�˳�����)��"))
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
    print score,"��Ϊ",grade,"��"
