#-*-coding:utf-8-*-
'''
Created on 2015��5��19��
Description��
@author:ECNU_zenwan
@version��
'''
sn=100
hn=float(sn/2)
for n in range(2,11):
    sn=sn+hn*2
    hn=hn/2
print("��10����ؾ���%.2f��\n��10�η����߶�Ϊ%.2f�ס�")%(sn,hn)